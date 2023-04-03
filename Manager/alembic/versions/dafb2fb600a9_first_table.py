"""First_table

Revision ID: dafb2fb600a9
Revises: 
Create Date: 2023-03-29 23:31:57.121589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dafb2fb600a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'measure',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('id_dispositivo', sa.String(50)),
        sa.Column('timestamp', sa.String(50)),
        sa.Column('kWh', sa.Float),
        
    )

def downgrade():
    op.drop_table('measure')