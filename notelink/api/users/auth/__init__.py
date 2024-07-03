from fastapi import APIRouter

from notelink.api.users.auth.backend import authentication_backend
from notelink.api.users.schemas import UserRead, UserCreate
from notelink.api.users.auth.views import fastapi_users
from notelink.core.settings.config import settings

router = APIRouter(prefix=settings.api.auth, tags=["Auth"])

router.include_router(
    fastapi_users.get_auth_router(
        authentication_backend,
    ),
)
router.include_router(
    fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)
