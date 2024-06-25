from datetime import datetime

from sqlalchemy.orm import Mapped

from notelink.core.models.base import Base


class Note(Base):
    title: Mapped[str]
    text: Mapped[str]
    expire: Mapped[datetime]
