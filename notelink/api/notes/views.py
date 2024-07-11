from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from fastapi_users.schemas import BaseUser
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.notes import crud
from notelink.api.notes.schemas import NoteSchema, NoteCreateSchema
from notelink.api.users.auth.dependencies import get_current_verified_user
from notelink.core.helpers import db_helper
from notelink.core.models.note import Note
from notelink.tools.errors import NotFound

router = APIRouter(tags=["Notes"])


@router.get(
    "/public/",
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


@router.get(
    "/public/{public_id}",
    response_model=NoteSchema,
    status_code=status.HTTP_200_OK,
)
async def get_public_note(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    public_id: str,
):
    public_notes = await session.execute(
        select(Note).filter(Note.public_id == public_id)
    )
    note = public_notes.scalars().first()
    if not note:
        raise NotFound()
    return note


@router.get(
    "/private/{private_id}",
    response_model=NoteSchema,
    status_code=status.HTTP_200_OK,
)
async def get_private_note(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    private_id: str,
    current_user: BaseUser = Depends(get_current_verified_user),
):
    private_notes = await session.execute(
        select(Note).filter(Note.private_id == private_id)
    )
    note = private_notes.scalars().first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return note
