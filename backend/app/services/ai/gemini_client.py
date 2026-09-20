from google import genai
from google.genai import types
from pydantic import BaseModel, Field

from app.core.config import settings


class ResumeAnalysis(BaseModel):
    overall_score: int = Field(
        description="Overall resume quality score from 0 to 100."
    )

    summary: str = Field(
        description="A concise professional summary of the resume."
    )

    strengths: list[str] = Field(
        description="The strongest aspects of the resume."
    )

    weaknesses: list[str] = Field(
        description="Important weaknesses or problems in the resume."
    )

    skills_detected: list[str] = Field(
        description="Technical and professional skills clearly detected in the resume."
    )

    missing_sections: list[str] = Field(
        description="Important resume sections that are missing or inadequate."
    )

    suggestions: list[str] = Field(
        description="Specific actionable improvements the candidate should make."
    )


client = genai.Client(api_key=settings.gemini_api_key)


async def analyze_resume(resume_text: str) -> ResumeAnalysis:
    prompt = f"""
You are a professional resume and ATS analyst.

Analyze the following resume thoroughly.

Evaluate:
- overall resume quality
- ATS compatibility
- clarity and professionalism
- skills
- experience/project presentation
- missing or weak sections
- actionable improvements

Be factual and specific. Do not invent information that is not present in the resume.

Return the analysis strictly according to the provided response schema.

RESUME:
{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ResumeAnalysis,
        ),
    )

    return ResumeAnalysis.model_validate_json(response.text)