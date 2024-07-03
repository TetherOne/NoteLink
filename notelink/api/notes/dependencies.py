from typing import Annotated

from fastapi import Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.notes import crud
from notelink.core.helpers import db_helper
from notelink.core.models.note import Note
from notelink.tools.errors import NotFound


async def note_by_id(
    note_id: Annotated[int, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
) -> Note:
    """
    Вспомогательная функция для
    получения Note по id
    """
    note = await crud.get_note(
        session=session,
        note_id=note_id,
    )
    if note is not None:
        return note
    raise NotFound()
