"""create songs table

Revision ID: 1b38ec67b151
Revises: d20818fe0d9d
Create Date: 2021-04-03 23:46:43.976454+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b38ec67b151'
down_revision = 'd20818fe0d9d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "songs",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("album_id", sa.Integer, sa.ForeignKey("albums.id", name="fk_songs_album_id"), nullable=False),
    )


def downgrade():
    op.drop_table("songs")
