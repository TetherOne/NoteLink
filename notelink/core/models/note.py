from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

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
    expire: Mapped[datetime]
    tags: Mapped[list["Tag"]] = relationship(
        secondary="note_tag_associations",
        back_populates="notes",
    )
