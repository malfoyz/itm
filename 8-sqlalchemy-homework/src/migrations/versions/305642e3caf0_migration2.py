"""migration2

Revision ID: 305642e3caf0
Revises: 4506afd598f3
Create Date: 2024-09-10 05:17:11.136102

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '305642e3caf0'
down_revision: Union[str, None] = '4506afd598f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('goods', 'supply_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('goods_supply_id_fkey', 'goods', type_='foreignkey')
    op.create_foreign_key(None, 'goods', 'supplies', ['supply_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'goods', type_='foreignkey')
    op.create_foreign_key('goods_supply_id_fkey', 'goods', 'supplies', ['supply_id'], ['id'])
    op.alter_column('goods', 'supply_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
