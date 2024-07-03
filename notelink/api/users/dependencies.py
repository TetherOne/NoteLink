from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users.authentication.strategy import DatabaseStrategy

from notelink.api.users.auth.user_manager import UserManager
from notelink.core.helpers import db_helper
from notelink.core.models import AccessToken, User
from notelink.core.settings.config import settings

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase


async def get_access_tokens_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
):
    yield AccessToken.get_db(session=session)


def get_database_strategy(
    access_tokens_db: Annotated[
        "AccessTokenDatabase[AccessToken]",
        Depends(get_access_tokens_db),
    ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_tokens_db,
        lifetime_seconds=settings.access_token.lifetime_seconds,
    )


async def get_users_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
):
    yield User.get_db(session=session)


async def get_user_manager(
    users_db: Annotated[
        "SQLAlchemyUserDatabase",
        Depends(get_users_db),
    ]
):
    yield UserManager(users_db)
