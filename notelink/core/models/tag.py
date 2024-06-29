from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from notelink.core.models import Base
from notelink.core.models.mixins import CreateTimeMixin

if TYPE_CHECKING:
    from notelink.core.models import Note


class Tag(
    Base,
    CreateTimeMixin,
):
    name: Mapped[str]
    notes: Mapped[list["Note"]] = relationship(
        secondary="note_tag_associations",
        back_populates="tags",
    )
