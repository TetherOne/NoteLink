from typing import Annotated

from fastapi import Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.tags import crud
from notelink.core.helpers import db_helper
from notelink.core.models import Tag
from notelink.tools.errors import NotFound


async def tag_by_id(
    tag_id: Annotated[int, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
) -> Tag:
    """
    Вспомогательная функция для
    получения Tag по id
    """
    tag = await crud.get_tag(
        session=session,
        tag_id=tag_id,
    )
    if tag is not None:
        return tag
    raise NotFound()
