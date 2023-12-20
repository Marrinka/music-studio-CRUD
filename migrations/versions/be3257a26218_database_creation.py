"""Database creation

Revision ID: be3257a26218
Revises: 
Create Date: 2023-12-16 21:14:51.716686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be3257a26218'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('surname', sa.Integer(), nullable=False),
                    sa.Column('phone', sa.Integer(), nullable=False),
                    sa.Column('birthdate', sa.TIMESTAMP(), nullable=True),
                    sa.Column('banned', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('instruments',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('type', sa.String(), nullable=False),
                    sa.Column('brand', sa.String(), nullable=False),
                    sa.Column('model', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rooms',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('square', sa.Integer(), nullable=False),
                    sa.Column('price', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('requests',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('clientt_id', sa.Integer(), nullable=True),
                    sa.Column('time_from', sa.TIMESTAMP(), nullable=False),
                    sa.Column('time_to', sa.TIMESTAMP(), nullable=False),
                    sa.Column('room_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['clientt_id'], ['clients.id'], ),
                    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
                    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('required_istruments',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('request_id', sa.Integer(), nullable=True),
                    sa.Column('instrument_type', sa.String(), nullable=False),
                    sa.ForeignKeyConstraint(['request_id'], ['requests.id'], ),
                    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('required_istruments')
    op.drop_table('requests')
    op.drop_table('rooms')
    op.drop_table('instruments')
    op.drop_table('clients')
    # ### end Alembic commands ###