from fastapi import APIRouter

from app.api.router import sample

api_router = APIRouter()
api_router.include_router(sample.router, prefix="/tests", tags=["tests"])
