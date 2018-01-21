"""empty message

Revision ID: 3cd43adecac7
Revises: 9f8a879ed013
Create Date: 2017-11-17 19:40:53.759093

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3cd43adecac7'
down_revision = '9f8a879ed013'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('author', 'is_author',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.add_column('blog__post', sa.Column('image', sa.String(length=255), nullable=True))
    op.alter_column('blog__post', 'live',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('blog__post', 'live',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.drop_column('blog__post', 'image')
    op.alter_column('author', 'is_author',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    # ### end Alembic commands ###
