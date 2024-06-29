"""ad unique for tag name

Revision ID: 79ae8d4c5857
Revises: 5a8c2dfc74db
Create Date: 2024-06-29 22:52:27.592218

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "79ae8d4c5857"
down_revision: Union[str, None] = "5a8c2dfc74db"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(None, "tags", ["name"])


def downgrade() -> None:
    op.drop_constraint(None, "tags", type_="unique")
