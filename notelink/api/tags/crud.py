from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.tags.schemas import TagCreateSchema
from notelink.core.models import Tag


async def get_tag(
    session: AsyncSession,
    tag_id: int,
) -> Tag | None:
    return await session.get(Tag, tag_id)


async def check_tag(
    session: AsyncSession,
    tag_name: str,
) -> bool:
    result = await session.execute(
        select(Tag).where(Tag.name == tag_name),
    )
    tag = result.scalar_one_or_none()
    return tag is None


async def create_tag(
    session: AsyncSession,
    tag_create: TagCreateSchema,
):
    tag = Tag(**tag_create.dict())
    session.add(tag)
    await session.commit()
    await session.refresh(tag)
    return tag
