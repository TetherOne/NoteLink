import datetime
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import (
    Integer,
    ForeignKey,
    String,
    DateTime,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from .base import Base
from ..types.user_id import UserId

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[UserId]):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[UserId] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False,
    )
    token: Mapped[str] = mapped_column(String(43), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.datetime.utcnow
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
