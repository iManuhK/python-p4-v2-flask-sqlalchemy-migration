"""rename department

Revision ID: 07064eddddb0
Revises: e9a6ef529904
Create Date: 2024-07-02 16:09:21.032485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07064eddddb0'
down_revision = 'e9a6ef529904'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
