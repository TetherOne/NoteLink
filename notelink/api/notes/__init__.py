from fastapi import APIRouter


from notelink.api.notes.views import router as notes_router
from notelink.core.settings.config import settings

router = APIRouter()

router.include_router(
    notes_router,
    prefix=settings.api.notes,
)
