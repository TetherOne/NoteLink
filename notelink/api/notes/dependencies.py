from typing import Annotated

from fastapi import Depends, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status

from notelink.api.notes import crud
from notelink.core.helpers import db_helper
from notelink.core.models import Note


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

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Note with {note_id} id not found.",
    )
