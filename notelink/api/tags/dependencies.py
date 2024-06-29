from typing import Annotated

from fastapi import Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.tags import crud
from notelink.core.helpers import db_helper
from notelink.core.models import Tag


async def tag_by_id(
    tag_id: Annotated[int, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
) -> Tag:
    """
    Вспомогательная функция для
    получения Resume по id
    """
    tag = await crud.get_tag(
        session=session,
        tag_id=tag_id,
    )
    if tag is not None:
        return tag
