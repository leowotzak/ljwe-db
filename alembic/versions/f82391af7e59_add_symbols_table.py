"""add symbols table

Revision ID: f82391af7e59
Revises: 22c52ab0c8cf
Create Date: 2021-11-12 13:29:08.970486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f82391af7e59'
down_revision = '22c52ab0c8cf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'equities',
        sa.Column('equity_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String),
        sa.Column('ticker', sa.String),
        sa.Column('description', sa.String),
        sa.Column('sector', sa.String),
        sa.Column('asset_type', sa.String),
        sa.Column('created_date', sa.DateTime),
        sa.Column('last_updated_date', sa.DateTime)
    )



def downgrade():
    op.drop_table('equities')
