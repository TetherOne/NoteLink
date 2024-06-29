from datetime import datetime

from pydantic import BaseModel


class TagBaseSchema(BaseModel):
    name: str


class TagSchema(TagBaseSchema):
    id: int
    created_at: datetime


class TagCreateSchema(TagBaseSchema):
    pass
