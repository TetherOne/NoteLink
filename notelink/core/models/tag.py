from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship, mapped_column

from notelink.core.models.base import Base
from notelink.core.models.mixins import CreateTimeMixin
from notelink.core.models.mixins.id_int_pk import IdIntPkMixin

if TYPE_CHECKING:
    from notelink.core.models.note import Note


class Tag(
    Base,
    IdIntPkMixin,
    CreateTimeMixin,
):
    name: Mapped[str] = mapped_column(unique=True)
    notes: Mapped[list["Note"]] = relationship(
        secondary="note_tag_associations",
        back_populates="tags",
    )
    count: Mapped[int] = mapped_column(default=1)
