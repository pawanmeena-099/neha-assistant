from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="Backend API for the NEHA AI Assistant",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "name": "NEHA",
        "status": "running",
        "version": "0.1.0",
        "environment": settings.app_env,
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "neha-backend",
    }


@app.get("/api/v1/status")
async def system_status():
    return {
        "assistant": "NEHA",
        "backend": "online",
        "ai_engine": "not_configured",
        "memory": "not_configured",
        "tools": "not_configured",
    }