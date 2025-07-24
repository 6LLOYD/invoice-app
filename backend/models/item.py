from config import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    quantite = db.Column(db.Integer, nullable=False)
    prix_unitaire = db.Column(db.Float, nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=True)
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'), nullable=False)