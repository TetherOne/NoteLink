import uuid
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.notes.schemas import NoteCreateSchema
from notelink.core.models import Note


async def get_notes(
    session: AsyncSession,
) -> Sequence[Note]:
    stmt = (
        select(Note).where(Note.private_url.is_(None)).order_by(Note.created_at.desc())
    )
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
    if note_create.is_public:
        url = f"http://notelink/public/note/{str(uuid.uuid4())}"
        private_url = None
    else:
        url = None
        private_url = f"http://notelink/private/note/{str(uuid.uuid4())}"
    note_data = note_create.dict()
    note_data["url"] = url
    note_data["private_url"] = private_url
    note = Note(**note_data)
    session.add(note)
    await session.commit()
    await session.refresh(note)
    return note
