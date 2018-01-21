"""empty message

Revision ID: d4577fb2156c
Revises: 
Create Date: 2017-11-14 19:09:36.378039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4577fb2156c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adminastor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=35), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=True),
    sa.Column('is_author', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('admin', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blog__post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('slug', sa.String(length=256), nullable=True),
    sa.Column('publish_date', sa.DateTime(), nullable=True),
    sa.Column('live', sa.Boolean(), nullable=True),
    sa.Column('category', sa.String(length=70), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog__post')
    op.drop_table('blog')
    op.drop_table('author')
    op.drop_table('adminastor')
    # ### end Alembic commands ###
