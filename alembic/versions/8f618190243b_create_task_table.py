"""create task table

Revision ID: 8f618190243b
Revises: 
Create Date: 2026-10-22 22:00:13.320588

"""

from alembic import op
import sqlalchemy as sa


revision = "1a2b3c4d5e6f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
  op.create_table(
      "tasks",
      sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
      sa.Column("title", sa.String(), nullable=False),
      sa.Column("done", sa.Boolean(), nullable=False),
      sa.PrimaryKeyConstraint("id"),
  )


def downgrade() -> None:
  op.drop_table("tasks")
