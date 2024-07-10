"""removed text to s3_key

Revision ID: 4bbf2ce11828
Revises: e7bacfe68aee
Create Date: 2024-07-09 22:20:34.836279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4bbf2ce11828"
down_revision: Union[str, None] = "e7bacfe68aee"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("notes", sa.Column("s3_key", sa.String(), nullable=False))
    op.drop_column("notes", "text")


def downgrade() -> None:
    op.add_column(
        "notes",
        sa.Column("text", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_column("notes", "s3_key")
