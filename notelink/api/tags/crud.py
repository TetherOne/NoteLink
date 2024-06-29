from sqlalchemy.ext.asyncio import AsyncSession

from notelink.api.tags.schemas import TagCreateSchema
from notelink.core.models import Tag


async def create_tag(
    session: AsyncSession,
    tag_create: TagCreateSchema,
):
    tag = Tag(**tag_create.dict())
    session.add(tag)
    await session.commit()
    await session.refresh(tag)
    return tag
