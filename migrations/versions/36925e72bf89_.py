"""empty message

Revision ID: 36925e72bf89
Revises: 6ce00a4e6adf
Create Date: 2021-09-27 14:21:36.896793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36925e72bf89'
down_revision = '6ce00a4e6adf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=10), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('level', sa.String(length=10), nullable=False),
    sa.Column('rdatetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###