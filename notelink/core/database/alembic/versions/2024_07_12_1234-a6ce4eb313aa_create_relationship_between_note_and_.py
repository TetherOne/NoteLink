"""create relationship between note and user

Revision ID: a6ce4eb313aa
Revises: e7bacfe68aee
Create Date: 2024-07-12 12:34:11.909376

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a6ce4eb313aa"
down_revision: Union[str, None] = "e7bacfe68aee"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("notes", sa.Column("user_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "notes", "users", ["user_id"], ["id"])


def downgrade() -> None:
    op.drop_constraint(None, "notes", type_="foreignkey")
    op.drop_column("notes", "user_id")
