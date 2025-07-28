from commands.delete_document_command import DeleteDocumentCommand
from services.document_service import DocumentService

class DeleteDocumentAction:
    @staticmethod
    def execute(command: DeleteDocumentCommand):
        if not command.document_id:
            raise ValueError("L'ID du document est requis")

        return DocumentService.delete_document(command.document_id)