"""ad counte to tag

Revision ID: 71d107f6c63e
Revises: 79ae8d4c5857
Create Date: 2024-06-29 23:21:24.152608

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "71d107f6c63e"
down_revision: Union[str, None] = "79ae8d4c5857"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("note_tag_associations", "count")
    op.add_column("tags", sa.Column("count", sa.Integer(), nullable=False))


def downgrade() -> None:
    op.drop_column("tags", "count")
    op.add_column(
        "note_tag_associations",
        sa.Column(
            "count",
            sa.INTEGER(),
            server_default=sa.text("1"),
            autoincrement=False,
            nullable=False,
        ),
    )
