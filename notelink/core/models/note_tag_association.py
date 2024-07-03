from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from notelink.core.models.base import Base
from notelink.core.models.mixins import CreateTimeMixin
from notelink.core.models.mixins.id_int_pk import IdIntPkMixin


class NoteTagAssociation(Base, IdIntPkMixin, CreateTimeMixin):
    __table_args__ = (
        UniqueConstraint(
            "note_id",
            "tag_id",
            name="idx_unique_note_tag",
        ),
    )

    note_id: Mapped[int] = mapped_column(
        ForeignKey("notes.id"),
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey("tags.id"),
    )
