"""initial script

Revision ID: 68adb7ce57dc
Revises: 
Create Date: 2021-09-12 15:14:38.832901

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '68adb7ce57dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

     # initialize `pgcrypto` extension for the CRUD to work
    op.execute(text("CREATE EXTENSION IF NOT EXISTS pgcrypto;"))

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uid', sqlalchemy_utils.types.uuid.UUIDType(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('master_pwd', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('uid')
    )
    op.create_table('passwords',
    sa.Column('pid', sqlalchemy_utils.types.uuid.UUIDType(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('site', sa.String(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('user_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.uid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('pid'),
    sa.UniqueConstraint('pid'),
    sa.UniqueConstraint('user_id', 'site', 'username', name='uniq_site_username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('passwords')
    op.drop_table('users')
    # ### end Alembic commands ###
