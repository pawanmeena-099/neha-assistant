from fastapi import FastAPI

app = FastAPI(
    title="NEHA Assistant API",
    description="Backend API for the NEHA AI Assistant",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "name": "NEHA",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "neha-backend",
    }