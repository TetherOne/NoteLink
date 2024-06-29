from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.notes.schemas import NoteCreateSchema
from notelink.core.models import Note


async def get_notes(
    session: AsyncSession,
) -> Sequence[Note]:
    stmt = select(Note).order_by(Note.created_at.desc())
    result = await session.scalars(stmt)
    return result.all()


async def get_note(
    session: AsyncSession,
    note_id: int,
) -> Note | None:
    return await session.get(Note, note_id)


async def create_note(
    session: AsyncSession,
    note_create: NoteCreateSchema,
):
    note = Note(**note_create.dict())
    session.add(note)
    await session.commit()
    await session.refresh(note)
    return note
