"""empty message

Revision ID: dd59eac73821
Revises: 73da46013424
Create Date: 2024-03-20 15:48:35.514969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd59eac73821'
down_revision = '73da46013424'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pizza_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('restaurant_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_restaurant_pizzas_restaurant_id_restaurants'), 'restaurants', ['restaurant_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_restaurant_pizzas_pizza_id_pizzas'), 'pizzas', ['pizza_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_restaurant_pizzas_pizza_id_pizzas'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_restaurant_pizzas_restaurant_id_restaurants'), type_='foreignkey')
        batch_op.drop_column('restaurant_id')
        batch_op.drop_column('pizza_id')

    # ### end Alembic commands ###
