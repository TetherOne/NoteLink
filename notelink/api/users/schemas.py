from fastapi_users import schemas

from notelink.core.models.types.user_id import UserId


class UserRead(schemas.BaseUser[UserId]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
