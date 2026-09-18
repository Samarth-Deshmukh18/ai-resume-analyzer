from sqlalchemy import text
from app.core.database import engine

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.auth import router as auth_router

app = FastAPI()
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        return {
            "message": "AI Resume Analyzer API is running",
            "database": result.scalar(),
        }