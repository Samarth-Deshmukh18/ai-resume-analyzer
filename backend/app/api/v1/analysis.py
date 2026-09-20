from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.resume import Resume
from app.models.analysis import Analysis
from app.services.ai.gemini_client import analyze_resume


router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"],
)


@router.post("/{resume_id}")
async def create_analysis(
    resume_id: int,
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

    if not resume.extracted_text:
        raise HTTPException(
            status_code=400,
            detail="No extracted text available for this resume",
        )

    analysis_result = await analyze_resume(resume.extracted_text)

    analysis = Analysis(
    resume_id=resume.id,
    score=analysis_result.overall_score,
    summary=analysis_result.summary,
    skills_detected="\n".join(
        f"- {item}" for item in analysis_result.skills_detected
    ),
    missing_sections="\n".join(
        f"- {item}" for item in analysis_result.missing_sections
    ),
    strengths="\n".join(
        f"- {item}" for item in analysis_result.strengths
    ),
    weaknesses="\n".join(
        f"- {item}" for item in analysis_result.weaknesses
    ),
    suggestions="\n".join(
        f"- {item}" for item in analysis_result.suggestions
    ),
)

    db.add(analysis)
    await db.commit()
    await db.refresh(analysis)

    return {
        "message": "Resume analyzed successfully",
        "analysis_id": analysis.id,
        "resume_id": resume.id,
        "result": analysis_result.model_dump(),
    }

@router.get("/{resume_id}")
async def get_analysis(
    resume_id: int,
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

    result = await db.execute(
        select(Analysis)
        .where(Analysis.resume_id == resume_id)
        .order_by(Analysis.id.desc())
    )

    analysis = result.scalars().first()

    if analysis is None:
        raise HTTPException(
            status_code=404,
            detail="No analysis found for this resume",
        )

    return {
        "analysis_id": analysis.id,
        "resume_id": analysis.resume_id,
        "score": analysis.score,
        "summary": analysis.summary,
        "skills_detected": analysis.skills_detected,
     "missing_sections": analysis.missing_sections,
        "strengths": analysis.strengths,
        "weaknesses": analysis.weaknesses,
        "suggestions": analysis.suggestions,
    }

@router.get("/")
async def get_analysis_history(
    current_user=Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Analysis)
        .join(Resume, Analysis.resume_id == Resume.id)
        .where(Resume.user_id == current_user.id)
        .order_by(Analysis.id.desc())
    )

    analyses = result.scalars().all()

    return [
        {
            "analysis_id": analysis.id,
            "resume_id": analysis.resume_id,
            "score": analysis.score,
            "Summary": analysis.summary,
            "skills_detected": analysis.skills_detected,
            "missing_sections": analysis.missing_sections,
            "strengths": analysis.strengths,
            "weaknesses": analysis.weaknesses,
            "suggestions": analysis.suggestions,
        }
        for analysis in analyses
    ]