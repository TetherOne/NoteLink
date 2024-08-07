from datetime import datetime
from pydantic import BaseModel


class NoteBaseSchema(BaseModel):
    title: str
    text: str | None = None
    is_public: bool
    user_id: int
    expire: datetime


class NoteSchema(NoteBaseSchema):
    id: int
    public_id: str | None
    private_id: str | None
    user_id: int | None
    created_at: datetime
    updated_at: datetime
    s3_key: str | None

    class Config:
        orm_mode = True
        from_attributes = True


class NoteCreateSchema(NoteBaseSchema):
    user_id: int | None = None
