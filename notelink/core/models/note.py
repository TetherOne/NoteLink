from datetime import datetime

from sqlalchemy.orm import Mapped, relationship

from notelink.core.models.base import Base
from notelink.core.models.mixins import CreateTimeMixin, UpdateTimeMixin


class Note(
    Base,
    CreateTimeMixin,
    UpdateTimeMixin,
):
    title: Mapped[str]
    text: Mapped[str]
    expire: Mapped[datetime]
    tags: Mapped[list[int]] = relationship(
        secondary="note_tag_associations",
        back_populates="notes",
    )
