from fastapi_users import FastAPIUsers

from .backend import authentication_backend
from .user_manager import get_user_manager
from ...core.models import User
from notelink.core.models.types.user_id import UserId

fastapi_users = FastAPIUsers[User, UserId](
    get_user_manager,
    [authentication_backend],
)
