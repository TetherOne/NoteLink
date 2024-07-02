from fastapi import APIRouter

from notelink.api.auth.schemas import UserRead, UserUpdate
from notelink.api.auth.user_routers import fastapi_users
from notelink.core.settings.config import settings

router = APIRouter(
    prefix=settings.api.users,
    tags=["Users"],
)

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
