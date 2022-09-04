"""initial commit

Revision ID: 0c5bd2e9a9ff
Revises: 
Create Date: 2022-09-04 08:08:34.077273

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel  # NEW


# revision identifiers, used by Alembic.
revision = "0c5bd2e9a9ff"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "general_earthquake",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("datetime", sa.DateTime(), nullable=False),
        sa.Column("latitude", sa.Numeric(precision=6, scale=2), nullable=True),
        sa.Column("longitude", sa.Numeric(precision=6, scale=2), nullable=True),
        sa.Column("magnitude", sa.Numeric(precision=6, scale=2), nullable=False),
        sa.Column("depth", sa.Numeric(precision=6, scale=2), nullable=False),
        sa.Column("region", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("country", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("city", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("distance", sa.Numeric(precision=6, scale=2), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("general_earthquake")
    # ### end Alembic commands ###
