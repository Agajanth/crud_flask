"""empty message

Revision ID: e30c78e34eae
Revises: aff0297a62e8
Create Date: 2021-06-22 19:51:03.792890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e30c78e34eae'
down_revision = 'aff0297a62e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'persona', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'persona', type_='unique')
    # ### end Alembic commands ###
