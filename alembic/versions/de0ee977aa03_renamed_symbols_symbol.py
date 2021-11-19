"""renamed symbols > symbol

Revision ID: de0ee977aa03
Revises: f928a49ef7ce
Create Date: 2021-11-18 23:15:36.551047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de0ee977aa03'
down_revision = 'f928a49ef7ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('symbol',
    sa.Column('symbol_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ticker', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('sector', sa.String(), nullable=True),
    sa.Column('asset_type', sa.String(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('last_updated_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('symbol_id')
    )
    op.drop_table('symbols')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('symbols',
    sa.Column('symbol_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('ticker', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('sector', sa.VARCHAR(), nullable=True),
    sa.Column('asset_type', sa.VARCHAR(), nullable=True),
    sa.Column('created_date', sa.DATETIME(), nullable=False),
    sa.Column('last_updated_date', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('symbol_id')
    )
    op.drop_table('symbol')
    # ### end Alembic commands ###
