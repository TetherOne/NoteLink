from fastapi_users import FastAPIUsers

from notelink.api.auth.backend import authentication_backend
from notelink.api.auth.dependencies import get_user_manager
from notelink.core.models import User
from notelink.core.models.types.user_id import UserId

fastapi_users = FastAPIUsers[User, UserId](
    get_user_manager,
    [authentication_backend],
)
