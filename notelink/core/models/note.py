from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from notelink.core.models.base import Base
from notelink.core.models.mixins import CreateTimeMixin, UpdateTimeMixin
from notelink.core.models.mixins.id_int_pk import IdIntPkMixin

if TYPE_CHECKING:
    from notelink.core.models.tag import Tag
    from notelink.core.models.user import User


class Note(
    Base,
    IdIntPkMixin,
    CreateTimeMixin,
    UpdateTimeMixin,
):
    title: Mapped[str]
    s3_key: Mapped[str | None]
    is_public: Mapped[bool] = mapped_column(default=True)
    public_id: Mapped[str | None]
    private_id: Mapped[str | None]
    expire: Mapped[datetime]
    tags: Mapped[list["Tag"]] = relationship(
        secondary="note_tag_associations",
        back_populates="notes",
    )
    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
    )
    user: Mapped["User"] = relationship(
        "User",
        back_populates="notes",
    )
