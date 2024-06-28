from fastapi import APIRouter

from notelink.core.settings.config import settings
from notelink.api.notes.views import router as notes_router

router = APIRouter(
    prefix=settings.api.full_prefix,
)
router.include_router(notes_router)
