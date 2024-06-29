from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.tags import crud
from notelink.api.tags.schemas import TagSchema, TagCreateSchema
from notelink.core.helpers import db_helper

router = APIRouter(tags=["Tags"])


@router.get(
    "/check/",
    response_model=bool,
)
async def check_tag_endpoint(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    tag_name: str,
) -> bool:
    return await crud.check_tag(
        session=session,
        tag_name=tag_name,
    )


@router.post(
    "/create/",
    response_model=TagSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_tag(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    tag_create: TagCreateSchema,
):
    return await crud.create_tag(
        session=session,
        tag_create=tag_create,
    )
