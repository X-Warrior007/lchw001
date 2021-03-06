"""del_email

Revision ID: fb04c0fdbe58
Revises: 9d67ea539a15
Create Date: 2018-03-13 16:17:20.359063

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fb04c0fdbe58'
down_revision = '9d67ea539a15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('email', table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', mysql.VARCHAR(length=32), nullable=True))
    op.create_index('email', 'users', ['email'], unique=True)
    # ### end Alembic commands ###
