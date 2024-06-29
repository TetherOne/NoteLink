"""ad count to note tag association table

Revision ID: 5a8c2dfc74db
Revises: a63c1907b162
Create Date: 2024-06-29 21:11:04.755158

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5a8c2dfc74db"
down_revision: Union[str, None] = "a63c1907b162"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "note_tag_associations",
        sa.Column("count", sa.Integer(), server_default="1", nullable=False),
    )


def downgrade() -> None:
    op.drop_column("note_tag_associations", "count")
