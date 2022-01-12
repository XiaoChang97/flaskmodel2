"""empty message

Revision ID: 6ce00a4e6adf
Revises: 
Create Date: 2021-09-22 14:13:51.333931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ce00a4e6adf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=12), nullable=False),
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
