from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.resume import Resume
from app.services.storage import supabase
from app.services.parsing.pdf_parser import extract_text_from_pdf
from app.services.parsing.docx_parser import extract_text_from_docx

router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"],
)


MAX_FILE_SIZE = 5 * 1024 * 1024
ALLOWED_EXTENSIONS = {".pdf", ".docx"}


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    filename = Path(file.filename or "").name
    extension = Path(filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF and DOCX files are allowed",
        )

    file_data = await file.read()
    extracted_text = None

    if extension == ".pdf":
        extracted_text = extract_text_from_pdf(file_data)
    elif extension == ".docx":
        extracted_text = extract_text_from_docx(file_data)
        

    if len(file_data) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File size must not exceed 5 MB",
        )

    storage_path = f"{current_user.id}/{uuid4()}_{filename}"

    content_type = (
        "application/pdf"
        if extension == ".pdf"
        else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

    try:
        supabase.storage.from_("resumes").upload(
            storage_path,
            file_data,
            {
                "content-type": content_type,
                "upsert": False,
            },
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to upload resume",
        )

    resume = Resume(
        user_id=current_user.id,
        filename=filename,
        file_path=storage_path,
        extracted_text=extracted_text,
    )

    db.add(resume)
    await db.commit()
    await db.refresh(resume)

    return {
        "message": "Resume uploaded successfully",
        "resume_id": resume.id,
        "filename": resume.filename,
    }

@router.get("/")
async def get_resumes(
    current_user=Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Resume)
        .where(Resume.user_id == current_user.id)
        .order_by(Resume.id.desc())
    )

    resumes = result.scalars().all()

    return [
        {
            "id": resume.id,
            "filename": resume.filename,
            "file_path": resume.file_path,
            "extracted_text": resume.extracted_text,
        }
        for resume in resumes
    ]