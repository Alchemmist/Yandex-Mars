"""добавили признак публикации

Revision ID: 07c7d0ff96cf
Revises: 
Create Date: 2023-04-15 08:26:44.829967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07c7d0ff96cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('is_published', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'is_published')
    # ### end Alembic commands ###
