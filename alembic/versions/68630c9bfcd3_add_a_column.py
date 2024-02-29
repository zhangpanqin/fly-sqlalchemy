"""Add a column

Revision ID: 68630c9bfcd3
Revises: 3b6254ad522a
Create Date: 2024-02-29 22:53:33.903119

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68630c9bfcd3'
down_revision: Union[str, None] = '3b6254ad522a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
