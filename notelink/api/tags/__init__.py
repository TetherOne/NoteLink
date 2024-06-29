from fastapi import APIRouter


from notelink.api.tags.views import router as tags_router
from notelink.core.settings.config import settings

router = APIRouter()

router.include_router(
    tags_router,
    prefix=settings.api.tags,
)
