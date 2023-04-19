"""empty message

Revision ID: 7a6908d87111
Revises: b906edae1b0b
Create Date: 2023-04-18 16:56:38.883629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a6908d87111'
down_revision = 'b906edae1b0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('barang',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kode_barang', sa.String(length=15), nullable=True),
    sa.Column('nama_barang', sa.String(length=30), nullable=True),
    sa.Column('harga_jual', sa.Integer(), nullable=True),
    sa.Column('harga_modal', sa.Integer(), nullable=True),
    sa.Column('tersedia', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('kode_barang')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('terjual',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('kode_barang', sa.String(length=15), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('terjual', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_terjual_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('terjual', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_terjual_timestamp'))

    op.drop_table('terjual')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    op.drop_table('barang')
    # ### end Alembic commands ###
