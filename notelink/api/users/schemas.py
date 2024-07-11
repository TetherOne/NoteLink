from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate

from notelink.core.models.types.user_id import UserId


class UserRead(BaseUser[UserId]):
    pass


class UserCreate(BaseUserCreate):
    pass


class UserUpdate(BaseUserUpdate):
    pass
