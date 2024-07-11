from fastapi import Depends
from fastapi_users.schemas import BaseUser

from notelink.api.users import fastapi_users
from notelink.tools.errors import NotAuthenticated


async def get_current_verified_user(
    current_user: BaseUser = Depends(
        fastapi_users.current_user(active=True, verified=True),
    )
):
    if not current_user:
        raise NotAuthenticated()
    return current_user
