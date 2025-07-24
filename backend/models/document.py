from config import db
import uuid

class Document(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    numero = db.Column(db.String(20), unique=True, nullable=False)
    date = db.Column(db.String(10), nullable=False)
    total = db.Column(db.Float, nullable=False)
    type_document = db.Column(db.String(20), nullable=False)
    statut = db.Column(db.String(20), default='Brouillon')
    client_id = db.Column(db.String(36), db.ForeignKey('client.id'), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=True)
    items = db.relationship('Item', backref='document', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'numero': self.numero,
            'date': self.date,
            'total': self.total,
            'type_document': self.type_document,
            'statut': self.statut,
            'client_id': self.client_id,
            'profile_id': self.profile_id
        }