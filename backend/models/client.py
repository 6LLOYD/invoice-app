from config import db
import uuid

class Client(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    telephone = db.Column(db.String(20), nullable=True)
    adresse_id = db.Column(db.String(36), db.ForeignKey('adresse.id'), nullable=True)
    
    def to_dict(self):
        return{
            'id' : self.id,
            'nom' : self.nom,
            'prenom' : self.prenom,
            'email' : self.email,
            'telephone' : self.telephone,
            'adresse_id' : self.adresse_id
        }