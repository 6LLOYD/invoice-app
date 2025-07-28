"""Renommage propre de devis_id en document_source_id avec FK nommée

Revision ID: ab7f3e28ed12
Revises: 71bc6aed9dc8
Create Date: 2025-07-28 13:12:14.669713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab7f3e28ed12'
down_revision = '71bc6aed9dc8'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('document', schema=None) as batch_op:
        # Renommage de la colonne
        batch_op.alter_column('devis_id', new_column_name='document_source_id')

        # Création de la nouvelle contrainte FK nommée
        batch_op.create_foreign_key(
            'fk_document_document_source_id',  # nom explicite
            'document',                        # table référencée
            ['document_source_id'],            # colonne locale
            ['id']                             # colonne distante
        )

    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('document', schema=None) as batch_op:
        # Supprimer la nouvelle FK
        batch_op.drop_constraint('fk_document_document_source_id', type_='foreignkey')

        # Revenir à l’ancien nom
        batch_op.alter_column('document_source_id', new_column_name='devis_id')

    # ### end Alembic commands ###
