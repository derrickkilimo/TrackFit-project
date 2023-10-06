"""InitialMigration

Revision ID: 5973521d87dd
Revises: 
Create Date: 2023-10-03 23:28:27.880979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5973521d87dd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "User",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("username", sa.String, unique=True, index=True),
    )

    op.create_table(
        "Workout",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("exercise_name", sa.String),
        sa.Column("duration_minutes", sa.Float),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id")),
    )


def downgrade() -> None:
    # Define the downgrade step if needed
    op.drop_table("workout")
    op.drop_table("user")
