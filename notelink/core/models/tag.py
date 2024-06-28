from sqlalchemy.orm import Mapped

from notelink.core.models import Base
from notelink.core.models.mixins import CreateTimeMixin


class Tag(
    Base,
    CreateTimeMixin,
):
    name: Mapped[str]
