"""ad is_public for note

Revision ID: 7a5b1ad6b686
Revises: 71d107f6c63e
Create Date: 2024-06-29 23:29:33.186505

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7a5b1ad6b686"
down_revision: Union[str, None] = "71d107f6c63e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("notes", sa.Column("is_public", sa.Boolean(), nullable=False))


def downgrade() -> None:
    op.drop_column("notes", "is_public")
