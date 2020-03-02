"""empty message

Revision ID: 39cacf7e31b7
Revises: e03616210d3c
Create Date: 2020-03-02 13:09:45.498685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39cacf7e31b7'
down_revision = 'e03616210d3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('linkname', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'linkname')
    # ### end Alembic commands ###