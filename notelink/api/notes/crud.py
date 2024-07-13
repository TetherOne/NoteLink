from datetime import datetime
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.notes.schemas import NoteCreateSchema
from notelink.core.models.note import Note
from notelink.core.s3.client import s3_client
from notelink.tools.utils import create_public_and_private


async def get_notes(
    session: AsyncSession,
) -> Sequence[Note]:
    notes = (
        select(Note).where(Note.private_id.is_(None)).order_by(Note.created_at.desc())
    )
    public_notes = await session.scalars(notes)
    return public_notes.all()


async def create_note(
    session: AsyncSession,
    note_create: NoteCreateSchema,
) -> Note:
    public_id, private_id = create_public_and_private(note_create)
    note_data = note_create.dict()
    note_data["public_id"] = public_id
    note_data["private_id"] = private_id

    # Генерация уникального имени файла для S3
    s3_key = f"{public_id}-{datetime.utcnow().isoformat()}.txt"
    await s3_client.upload_text(note_create.text, s3_key)
    note_data["s3_key"] = s3_key

    # Удаляем текст, так как он теперь в S3
    del note_data["text"]

    note = Note(**note_data)
    session.add(note)
    await session.commit()
    await session.refresh(note)
    return note
