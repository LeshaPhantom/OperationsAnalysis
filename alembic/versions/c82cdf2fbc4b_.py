"""empty message

Revision ID: c82cdf2fbc4b
Revises: 
Create Date: 2023-09-03 09:51:34.653295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c82cdf2fbc4b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Mytest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_time_operation', sa.String(length=20), nullable=False),
    sa.Column('data_payment', sa.String(length=10), nullable=False),
    sa.Column('card_number', sa.String(length=5), nullable=False),
    sa.Column('status_operation', sa.Boolean(), nullable=False),
    sa.Column('sum_operation', sa.String(length=30), nullable=False),
    sa.Column('currency_operation', sa.String(length=10), nullable=False),
    sa.Column('sum_payment', sa.String(length=30), nullable=False),
    sa.Column('currency_payment', sa.String(length=10), nullable=False),
    sa.Column('cashback', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=30), nullable=False),
    sa.Column('mss', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=30), nullable=False),
    sa.Column('bonus_cashback', sa.String(length=30), nullable=False),
    sa.Column('rounding_invest', sa.String(length=30), nullable=False),
    sa.Column('rounding_operation', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operation')
    op.drop_table('Mytest')
    # ### end Alembic commands ###
