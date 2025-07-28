from config import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Lien vers le service d’origine
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=True)

    # Infos "snapshotées" depuis Service
    description_service = db.Column(db.String(200))
    reference_snapshot = db.Column(db.String(50))  # <= AJOUT ICI
    prix_unitaire_snapshot = db.Column(db.Float)

    # Infos spécifiques à ce document
    surface = db.Column(db.Float, nullable=True)
    unite = db.Column(db.String(20), default="m²")
    prix_unitaire = db.Column(db.Float, nullable=False)
    montant = db.Column(db.Float, nullable=False)

    description = db.Column(db.String(200), nullable=False)  # ligne personnalisée
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'), nullable=False)
