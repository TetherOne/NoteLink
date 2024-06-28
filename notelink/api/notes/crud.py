from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.notes.schemas import NoteCreateSchema
from notelink.core.models import Note


async def create_note(
    session: AsyncSession,
    note_create: NoteCreateSchema,
):
    note = Note(**note_create.dict())
    session.add(note)
    await session.commit()
    await session.refresh(note)
    return note
