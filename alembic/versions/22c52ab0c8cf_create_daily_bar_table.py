"""create daily bar table

Revision ID: 22c52ab0c8cf
Revises: 
Create Date: 2021-11-12 13:20:17.622191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22c52ab0c8cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'daily_bar',
        sa.Column('timestamp', sa.DateTime, primary_key=True),
        sa.Column('symbol_id', sa.Integer, primary_key=True),
        sa.Column('open_price', sa.Float),
        sa.Column('high_price', sa.Float),
        sa.Column('low_price', sa.Float),
        sa.Column('close_price', sa.Float),
        sa.Column('adj_close_price', sa.Float),
        sa.Column('volume', sa.Float),
        sa.Column('dividend_amount', sa.Float),
        sa.Column('created_date', sa.DateTime),
        sa.Column('last_updated_date', sa.DateTime),
    )

def downgrade():
    op.drop_table('daily_bar')
