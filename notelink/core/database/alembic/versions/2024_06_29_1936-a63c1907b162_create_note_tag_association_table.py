"""create note_tag_association table

Revision ID: a63c1907b162
Revises: fe8bb8b9e620
Create Date: 2024-06-29 19:36:38.887316

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a63c1907b162"
down_revision: Union[str, None] = "fe8bb8b9e620"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "note_tag_associations",
        sa.Column("note_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["note_id"],
            ["notes.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tags.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("note_id", "tag_id", name="idx_unique_note_tag"),
    )


def downgrade() -> None:
    op.drop_table("note_tag_associations")
