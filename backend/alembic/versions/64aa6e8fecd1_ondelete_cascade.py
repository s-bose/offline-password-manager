"""ondelete cascade

Revision ID: 64aa6e8fecd1
Revises: e68039eaa315
Create Date: 2021-09-10 10:59:03.829572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64aa6e8fecd1'
down_revision = 'e68039eaa315'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('passwords_user_id_fkey', 'passwords', type_='foreignkey')
    op.create_foreign_key(None, 'passwords', 'users', ['user_id'], ['uid'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'passwords', type_='foreignkey')
    op.create_foreign_key('passwords_user_id_fkey', 'passwords', 'users', ['user_id'], ['uid'])
    # ### end Alembic commands ###
