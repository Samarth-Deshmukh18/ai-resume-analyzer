from sqlalchemy import text
from app.core.database import engine

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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