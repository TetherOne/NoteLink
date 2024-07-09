from datetime import datetime

from pydantic import BaseModel


class NoteBaseSchema(BaseModel):
    title: str
    text: str
    is_public: bool
    expire: datetime


class NoteSchema(NoteBaseSchema):
    id: int
    public_id: str | None
    private_id: str | None
    created_at: datetime
    updated_at: datetime


class NoteCreateSchema(NoteBaseSchema):
    pass


class NoteUpdateSchema(NoteBaseSchema):
    title: str | None = None
    text: str | None = None
    is_public: bool | None = None
    expire: datetime | None = None
