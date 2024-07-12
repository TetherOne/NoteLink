from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)
from sqlalchemy.orm import Mapped, relationship

from notelink.core.models.base import Base
from notelink.core.models.mixins.id_int_pk import IdIntPkMixin
from notelink.core.models.types.user_id import UserId

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from notelink.core.models.note import Note


class User(
    Base,
    IdIntPkMixin,
    SQLAlchemyBaseUserTable[UserId],
):
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)

    notes: Mapped[list["Note"]] = relationship(back_populates="user")
