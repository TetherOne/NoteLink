from datetime import datetime
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.notes.schemas import NoteCreateSchema, NoteSchema
from notelink.core.models.note import Note
from notelink.core.s3 import s3_client
from notelink.tools.utils import create_public_and_private


async def get_notes(
    session: AsyncSession,
) -> Sequence[NoteSchema]:
    notes_query = (
        select(Note).where(Note.private_id.is_(None)).order_by(Note.created_at.desc())
    )
    public_notes = await session.scalars(notes_query)
    notes = public_notes.all()

    notes_data = []
    for note in notes:
        note_data = NoteSchema.from_orm(note).dict()
        if note.s3_key:
            note_data["text"] = await s3_client.get_text(note.s3_key)
        notes_data.append(NoteSchema(**note_data))

    return notes_data


async def create_note(
    session: AsyncSession,
    note_create: NoteCreateSchema,
) -> Note:
    public_id, private_id = create_public_and_private(note_create)
    note_data = note_create.dict()
    note_data["public_id"] = public_id
    note_data["private_id"] = private_id

    s3_key = f"{public_id}-{datetime.utcnow().isoformat()}.txt"
    await s3_client.upload_text(note_create.text, s3_key)
    note_data["s3_key"] = s3_key

    del note_data["text"]

    note = Note(**note_data)
    session.add(note)
    await session.commit()
    await session.refresh(note)
    return note
