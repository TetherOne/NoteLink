from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship, mapped_column

from notelink.core.models.base import Base
from notelink.core.models.mixins import CreateTimeMixin, UpdateTimeMixin

if TYPE_CHECKING:
    from notelink.core.models import Tag


class Note(
    Base,
    CreateTimeMixin,
    UpdateTimeMixin,
):
    title: Mapped[str]
    text: Mapped[str]
    is_public: Mapped[bool] = mapped_column(default=True)
    url: Mapped[str | None]
    private_url: Mapped[str | None]
    expire: Mapped[datetime]
    tags: Mapped[list["Tag"]] = relationship(
        secondary="note_tag_associations",
        back_populates="notes",
    )
