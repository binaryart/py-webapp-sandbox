"""create albums table

Revision ID: d20818fe0d9d
Revises:
Create Date: 2021-04-03 23:22:47.867983+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d20818fe0d9d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "albums",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("guid", sa.String(32), unique=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("artist", sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_table("albums")
