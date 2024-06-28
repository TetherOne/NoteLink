from datetime import datetime

from sqlalchemy.orm import Mapped

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
