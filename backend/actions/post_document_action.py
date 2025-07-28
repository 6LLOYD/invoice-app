from commands.post_document_command import PostDocumentCommand
from services.document_service import DocumentService

class PostDocumentAction:
    @staticmethod
    def execute(command: PostDocumentCommand):
        if not command.numero or not command.date or command.total_ht is None:
            raise ValueError("Numéro, date et total_ht sont requis")

        if command.total_ht < 0:
            raise ValueError("Le total_ht ne peut pas être négatif")

        # Tu peux ajouter la validation Enum pour type_document ici si besoin

        # Calculer la TVA si non fournie
        if command.tva_montant is None:
            command.tva_montant = command.total_ht * (command.tva_taux / 100)

        if command.total_ttc is None:
            command.total_ttc = command.total_ht + command.tva_montant

        return DocumentService.post_document(command)
