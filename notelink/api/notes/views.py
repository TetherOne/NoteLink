from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.notes import crud
from notelink.api.notes.schemas import NoteSchema, NoteCreateSchema
from notelink.core.helpers import db_helper

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
