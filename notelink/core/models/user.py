from fastapi_users.db import SQLAlchemyBaseUserTable


from notelink.core.models import Base
from notelink.core.models.mixins import CreateTimeMixin


class User(
    Base,
    CreateTimeMixin,
    SQLAlchemyBaseUserTable[int],
):
    pass
