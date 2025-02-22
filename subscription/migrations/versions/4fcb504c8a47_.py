"""empty message

Revision ID: 4fcb504c8a47
Revises: 23c17475112c
Create Date: 2019-09-24 17:15:18.565747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fcb504c8a47'
down_revision = '23c17475112c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriptions', sa.Column('email', sa.String(length=50), nullable=True))
    op.drop_constraint(u'subscriptions_email_address_key', 'subscriptions', type_='unique')
    op.create_unique_constraint(None, 'subscriptions', ['email'])
    op.drop_column('subscriptions', 'email_address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriptions', sa.Column('email_address', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'subscriptions', type_='unique')
    op.create_unique_constraint(u'subscriptions_email_address_key', 'subscriptions', ['email_address'])
    op.drop_column('subscriptions', 'email')
    # ### end Alembic commands ###
