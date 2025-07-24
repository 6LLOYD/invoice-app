from commands.post_document_command import PostDocumentCommand
from services.document_service import DocumentService

class PostDocumentAction:
    @staticmethod
    def execute(command: PostDocumentCommand):
        if not command.numero or not command.date:
            raise ValueError("Numéro et date sont requis")
        if command.total < 0:
            raise ValueError("Le total ne peut pas être négatif")
        return DocumentService.post_document(command)