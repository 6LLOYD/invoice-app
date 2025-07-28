from commands.post_document_command import PostDocumentCommand
from services.document_service import DocumentService
from models.document_type import DocumentType  # ← Import l'enum

class PostDocumentAction:
    @staticmethod
    def execute(command: PostDocumentCommand):
        if not command.numero or not command.date or command.total_ht is None:
            raise ValueError("Numéro, date et total_ht sont requis")

        if command.total_ht < 0:
            raise ValueError("Le total_ht ne peut pas être négatif")

        # Vérification de la validité de l'enum
        try:
            command.type_document = DocumentType[command.type_document.upper()]
        except (KeyError, AttributeError):
            raise ValueError(f"Type de document invalide. Valeurs autorisées : {[e.name for e in DocumentType]}")

        # Calcul de la TVA si elle n'est pas fournie
        if command.tva_montant is None:
            command.tva_montant = command.total_ht * (command.tva_taux / 100)

        if command.total_ttc is None:
            command.total_ttc = command.total_ht + command.tva_montant

        return DocumentService.post_document(command)
