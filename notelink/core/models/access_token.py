from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTable,
)

from notelink.core.models import Base
from notelink.core.types.user_id import UserId


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[UserId]):
    pass


# async def get_access_token_db(
#     session: AsyncSession = Depends(get_async_session),
# ):
#     yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
