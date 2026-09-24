from fastapi import APIRouter, Depends, HTTPException
from app.schemas.job_match import JobDescriptionRequest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.resume import Resume
from app.models.job_match import JobMatch
from app.services.ai.job_match_client import analyze_job_match

router = APIRouter(
    prefix="/job-match",
    tags=["Job Match"],
)

@router.post("/{resume_id}")
async def create_job_match(
    resume_id: int,
    data: JobDescriptionRequest,
    current_user=Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Resume).where(
            Resume.id == resume_id,
            Resume.user_id == current_user.id,
        )
    )

    resume = result.scalar_one_or_none()

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found",
        )

    match_result = await analyze_job_match(
    resume_text=resume.extracted_text,
    job_description=data.job_description,
)

    job_match = JobMatch(
        resume_id=resume.id,
        job_description=data.job_description,
        match_score=match_result.match_score,
        matching_skills="\n".join(
            f"- {item}" for item in match_result.matching_skills
        ),
        missing_skills="\n".join(
            f"- {item}" for item in match_result.missing_skills
        ),
        experience_alignment=match_result.experience_alignment,
        suggestions="\n".join(
            f"- {item}" for item in match_result.suggestions
        ),
    )

    db.add(job_match)
    await db.commit()
    await db.refresh(job_match)

    return {
        "message": "Job description matched successfully",
        "job_match_id": job_match.id,
        "resume_id": resume.id,
        "result": match_result.model_dump(),
    }
        