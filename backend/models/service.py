from config import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String(200), nullable=True)  # <= AJOUT ICI
    description = db.Column(db.String(200), nullable=True)
    prix_defaut = db.Column(db.Float, nullable=True)