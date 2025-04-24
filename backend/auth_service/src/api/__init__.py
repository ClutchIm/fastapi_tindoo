from fastapi import APIRouter

from .dependencies import AsyncSessionDep
from src.api.v1 import router as books_router

router = APIRouter()

router.include_router(books_router)
