"""removed text to s3_key

Revision ID: 5e45f58dab25
Revises: a6ce4eb313aa
Create Date: 2024-07-13 22:17:50.891724

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5e45f58dab25"
down_revision: Union[str, None] = "a6ce4eb313aa"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("notes", sa.Column("s3_key", sa.String(), nullable=True))
    op.drop_column("notes", "text")


def downgrade() -> None:
    op.add_column(
        "notes",
        sa.Column("text", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_column("notes", "s3_key")
