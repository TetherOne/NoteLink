from datetime import datetime

from pydantic import BaseModel, field_validator


class TagBaseSchema(BaseModel):
    name: str


class TagSchema(TagBaseSchema):
    id: int
    created_at: datetime


class TagCreateSchema(TagBaseSchema):
    @field_validator("name")
    def lowercase_name(cls, value: str) -> str:
        return value.lower()
