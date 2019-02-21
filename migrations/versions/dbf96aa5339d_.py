"""empty message

Revision ID: dbf96aa5339d
Revises: 3dfc289fb54e
Create Date: 2019-02-19 19:43:26.525405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbf96aa5339d'
down_revision = '3dfc289fb54e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('posts_writer_fkey', 'posts', type_='foreignkey')
    op.drop_column('posts', 'writer')
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    op.add_column('posts', sa.Column('writer', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('posts_writer_fkey', 'posts', 'users', ['writer'], ['id'])
    # ### end Alembic commands ###
