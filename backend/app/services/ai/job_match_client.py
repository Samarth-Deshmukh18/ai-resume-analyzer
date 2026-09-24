from google import genai
from google.genai import types
from pydantic import BaseModel, Field

from app.core.config import settings


class JobMatchResult(BaseModel):
    match_score: int = Field(description="Match score from 0-100")
    matching_skills: list[str]
    missing_skills: list[str]
    experience_alignment: str
    suggestions: list[str]


client = genai.Client(api_key=settings.gemini_api_key)

async def analyze_job_match(
    resume_text: str,
    job_description: str,
) -> JobMatchResult:
    prompt = f"""
You are an ATS and recruitment expert.

Compare the resume against the job description.

Return:
- match score (0-100)
- matching skills
- missing skills
- experience alignment
- actionable suggestions

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=JobMatchResult,
        ),
    )

    return JobMatchResult.model_validate_json(response.text)