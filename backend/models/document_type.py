import enum
from sqlalchemy import Enum

class DocumentType(enum.Enum):
    DEVIS = "Devis"
    FACTURE = "Facture"
