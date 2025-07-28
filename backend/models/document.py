from config import db
import uuid
from .document_type import DocumentType  # si tu mets l'enum dans un fichier séparé

class Document(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    numero = db.Column(db.String(20), unique=True, nullable=False)
    date = db.Column(db.String(10), nullable=False)
    total_ht = db.Column(db.Float, nullable=False)
    tva_taux = db.Column(db.Float, default=5.5)
    tva_montant = db.Column(db.Float)
    total_ttc = db.Column(db.Float)

    type_document = db.Column(db.Enum(DocumentType), nullable=False)  # Enum
    version = db.Column(db.Integer, default=1)  # version simple
    statut = db.Column(db.String(20), default='Brouillon')
    adresse_chantier = db.Column(db.String(255), nullable=True)

    # Snapshot infos client
    nom_client = db.Column(db.String(100))
    email_client = db.Column(db.String(120))
    telephone_client = db.Column(db.String(20))
    adresse_client = db.Column(db.String(255))  # Tu peux concaténer rue + ville + CP + pays

    # Lien vers le client d'origine
    client_id = db.Column(db.String(36), db.ForeignKey('client.id'), nullable=False)
    # Lien vers l'émetteur
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=True)

    # Lien vers le devis source
    document_source_id = db.Column(
        db.String(36),
        db.ForeignKey('document.id', name='fk_document_document_source_id'),
        nullable=True
    )
    document_source = db.relationship("Document", remote_side=[id])


    items = db.relationship('Item', backref='document', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'numero': self.numero,
            'date': self.date,
            'total_ht': self.total_ht,
            'tva_taux': self.tva_taux,
            'tva_montant': self.tva_montant,
            'total_ttc': self.total_ttc,
            'type_document': self.type_document.name if self.type_document else None,
            'version': self.version,
            'statut': self.statut,
            'adresse_chantier': self.adresse_chantier,
            'nom_client': self.nom_client,
            'email_client': self.email_client,
            'telephone_client': self.telephone_client,
            'adresse_client': self.adresse_client,
            'client_id': self.client_id,
            'profile_id': self.profile_id,
            'document_source_id': self.document_source_id,
        }
