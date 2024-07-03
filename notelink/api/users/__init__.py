from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from notelink.api.users.auth import authentication_backend, UserRead
from notelink.api.users.dependencies import get_user_manager
from notelink.api.users.schemas import UserUpdate
from notelink.core.models import User
from notelink.core.models.types.user_id import UserId
from notelink.core.settings.config import settings

router = APIRouter(prefix=settings.api.auth, tags=["Users"])

fastapi_users = FastAPIUsers[User, UserId](
    get_user_manager,
    [authentication_backend],
)


router.include_router(
    fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
