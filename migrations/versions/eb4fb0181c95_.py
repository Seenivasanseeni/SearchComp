"""empty message

Revision ID: eb4fb0181c95
Revises: 0d91226c09bd
Create Date: 2019-05-02 21:50:55.969631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb4fb0181c95'
down_revision = '0d91226c09bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('website', sa.String(length=128), nullable=True),
    sa.Column('mission', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_organization_name'), 'organization', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_organization_name'), table_name='organization')
    op.drop_table('organization')
    # ### end Alembic commands ###