from config import db

class Adresse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rue = db.Column(db.String(200), nullable=False)
    ville = db.Column(db.String(100), nullable=False)
    code_postal = db.Column(db.String(20), nullable=False)
    pays = db.Column(db.String(100), nullable=False)