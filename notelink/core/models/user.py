from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from notelink.core.models import Base
from notelink.core.models.mixins import CreateTimeMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(
    Base,
    CreateTimeMixin,
    SQLAlchemyBaseUserTable[int],
):
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
