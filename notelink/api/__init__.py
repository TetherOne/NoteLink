from fastapi import APIRouter

from notelink.core.settings.config import settings
from notelink.api.notes import router as notes_router
from notelink.api.tags import router as tags_router
from notelink.api.users.auth import router as auth_router

router = APIRouter(
    prefix=settings.api.full_prefix,
)
router.include_router(notes_router)
router.include_router(tags_router)
router.include_router(auth_router)
