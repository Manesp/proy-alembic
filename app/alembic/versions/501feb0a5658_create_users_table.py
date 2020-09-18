"""create users table

Revision ID: 501feb0a5658
Revises: 
Create Date: 2020-09-10 23:29:28.720674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '501feb0a5658'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('age', sa.Integer),
    )


def downgrade():
    pass
