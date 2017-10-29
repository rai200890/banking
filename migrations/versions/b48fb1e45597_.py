"""empty message

Revision ID: b48fb1e45597
Revises: 373bff7e93ec
Create Date: 2017-10-28 22:24:57.185793

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b48fb1e45597'
down_revision = '373bff7e93ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('entity', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('parameters', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='event_pkey'),
    sa.UniqueConstraint('entity', name='event_entity_key')
    )
    # ### end Alembic commands ###
