"""rename columns

Revision ID: 1d4bc6e1bdfe
Revises: 90b48c85d7d7
Create Date: 2024-07-01 13:29:00.428244

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1d4bc6e1bdfe"
down_revision: Union[str, None] = "90b48c85d7d7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("notes", sa.Column("public_id", sa.String(), nullable=True))
    op.add_column("notes", sa.Column("private_id", sa.String(), nullable=True))
    op.drop_column("notes", "private_url")
    op.drop_column("notes", "url")


def downgrade() -> None:
    op.add_column(
        "notes",
        sa.Column("url", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "notes",
        sa.Column("private_url", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.drop_column("notes", "private_id")
    op.drop_column("notes", "public_id")
