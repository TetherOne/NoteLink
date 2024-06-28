from datetime import datetime

from sqlalchemy.orm import Mapped

from notelink.core.models.base import Base
from notelink.core.models.mixins.create_time import CreateTimeMixin
from notelink.core.models.mixins.update_time import UpdateTimeMixin


class Note(
    Base,
    CreateTimeMixin,
    UpdateTimeMixin,
):
    title: Mapped[str]
    text: Mapped[str]
    expire: Mapped[datetime]
