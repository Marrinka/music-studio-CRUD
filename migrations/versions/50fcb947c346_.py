"""Update clients table

Revision ID: 50fcb947c346
Revises: be3257a26218
Create Date: 2023-12-17 13:56:12.006232

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50fcb947c346'
down_revision: Union[str, None] = 'be3257a26218'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clients', sa.Column('email', sa.String(), nullable=False))
    op.add_column('clients', sa.Column('hashed_password', sa.String(length=1024), nullable=False))
    op.add_column('clients', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.add_column('clients', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    op.add_column('clients', sa.Column('is_verified', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('clients', 'is_verified')
    op.drop_column('clients', 'is_superuser')
    op.drop_column('clients', 'is_active')
    op.drop_column('clients', 'hashed_password')
    op.drop_column('clients', 'email')
    # ### end Alembic commands ###
