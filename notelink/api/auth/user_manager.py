from typing import Annotated, TYPE_CHECKING

from fastapi import Depends

from notelink.api.auth.users import get_users_db
from notelink.core.authentication.user_manager import UserManager

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


async def get_user_manager(
    users_db: Annotated["SQLAlchemyUserDatabase", Depends(get_users_db)],
):
    yield UserManager(users_db)
