from config import db
from models.client import Client

class ClientService:
    @staticmethod
    def post_client(command):
        client = Client(
            nom = command.nom,
            prenom = command.prenom,
            email = command.email,
            telephone = command.telephone,
            adresse_id = command.adresse_id
        )
        db.session.add(client)
        db.session.commit()
        return client
    