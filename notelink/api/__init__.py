from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from notelink.core.settings.config import settings
from notelink.api.notes import router as notes_router
from notelink.api.tags import router as tags_router
from notelink.api.users.auth import router as auth_router
from notelink.api.users import router as users_router


http_bearer = HTTPBearer(auto_error=False)
router = APIRouter(
    prefix=settings.api.full_prefix,
    dependencies=[Depends(http_bearer)],
)

router.include_router(notes_router)
router.include_router(tags_router)
router.include_router(auth_router)
router.include_router(users_router)
