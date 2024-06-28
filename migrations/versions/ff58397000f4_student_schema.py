"""Student Schema

Revision ID: ff58397000f4
Revises: 
Create Date: 2024-06-28 22:41:53.768776

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff58397000f4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Define the student table schema
    op.create_table(
        'student',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nombre', sa.String(20), nullable=False),
        sa.Column('apellido', sa.String(20), nullable=False),
        sa.Column('identificacion', sa.String(10), unique=True, nullable=False),
        sa.Column('edad', sa.Integer(), nullable=False),
        sa.Column('afinidad_magica', sa.String(20), nullable=False),
    )


def downgrade() -> None:
    # Drop the student table
    op.drop_table('student')