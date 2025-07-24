from config import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_entreprise = db.Column(db.String(100), nullable=False)
    ntva = db.Column(db.String(20), nullable=True)
    siret = db.Column(db.String(20), nullable=True)
    code_ape = db.Column(db.String(10), nullable=True)
    nrge = db.Column(db.String(20), nullable=True)
    travaux_sous_garantie_decennale = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    telephone = db.Column(db.String(20), nullable=True)
    adresse_id = db.Column(db.Integer, db.ForeignKey('adresse.id'), nullable=False)