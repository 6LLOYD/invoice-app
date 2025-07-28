from config import db
from models.document import Document

class DocumentService:
    @staticmethod
    def post_document(command):
        document = Document(
            numero=command.numero,
            date=command.date,
            total_ht=command.total_ht,
            tva_taux=command.tva_taux,
            tva_montant=command.tva_montant,
            total_ttc=command.total_ttc,
            type_document=command.type_document,
            client_id=command.client_id,
            profile_id=command.profile_id,
            statut=command.statut,
            adresse_chantier=command.adresse_chantier,
            nom_client=command.nom_client,
            email_client=command.email_client,
            telephone_client=command.telephone_client,
            adresse_client=command.adresse_client,
            document_source_id=command.document_source_id
        )
        db.session.add(document)
        db.session.commit()
        return document
    
    @staticmethod
    def get_document(document_id):
        return Document.query.get(document_id)
    
    @staticmethod
    def update_document(document_id, update_data):
        document = Document.query.get(document_id)
        if not document:
            raise Exception("Document non trouvé")

        # Exemple simple de mise à jour, tu peux adapter selon les champs autorisés
        for key, value in update_data.items():
            if hasattr(document, key):
                setattr(document, key, value)

        db.session.commit()
        return document
    
    @staticmethod
    def delete_document(document_id: str):
        document = Document.query.get(document_id)
        if not document:
            raise ValueError("Document introuvable")

        db.session.delete(document)
        db.session.commit()