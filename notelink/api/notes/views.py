from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.notes import crud
from notelink.api.notes.dependencies import note_by_id
from notelink.api.notes.schemas import NoteSchema, NoteCreateSchema
from notelink.core.helpers import db_helper
from notelink.core.models import Note

router = APIRouter(tags=["Notes"])


@router.get(
    "/",
    response_model=list[NoteSchema],
    status_code=status.HTTP_200_OK,
)
async def get_notes(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await crud.get_notes(
        session=session,
    )


@router.get(
    "/{note_id}/",
    response_model=NoteSchema,
    status_code=status.HTTP_200_OK,
)
async def get_note(
    note: Note = Depends(note_by_id),
):
    return note


@router.post(
    "/create/",
    response_model=NoteSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_note(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    note_create: NoteCreateSchema,
):
    return await crud.create_note(
        note_create=note_create,
        session=session,
    )


@router.get("/public/note/{note_id}", response_model=NoteSchema)
async def get_public_note(
    note_id: str,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    result = await session.execute(
        select(Note).filter(Note.url == f"http://notelink/public/note/{note_id}")
    )
    note = result.scalars().first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.get("/note/{note_id}", response_model=NoteSchema)
async def get_private_note(
    note_id: str,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    result = await session.execute(
        select(Note).filter(
            Note.private_url == f"http://notelink/private/note/{note_id}"
        )
    )
    note = result.scalars().first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
