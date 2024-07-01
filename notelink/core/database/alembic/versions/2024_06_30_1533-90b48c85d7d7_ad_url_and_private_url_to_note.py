"""ad url and private_url to note

Revision ID: 90b48c85d7d7
Revises: 7a5b1ad6b686
Create Date: 2024-06-30 15:33:29.226973

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "90b48c85d7d7"
down_revision: Union[str, None] = "7a5b1ad6b686"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("notes", sa.Column("url", sa.String(), nullable=True))
    op.add_column("notes", sa.Column("private_url", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("notes", "private_url")
    op.drop_column("notes", "url")
