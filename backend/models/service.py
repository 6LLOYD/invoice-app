from config import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    prix_defaut = db.Column(db.Float, nullable=True)