from commands.patch_document_command import PatchDocumentCommand
from services.document_service import DocumentService

class PatchDocumentAction:
    @staticmethod
    def execute(command: PatchDocumentCommand):
        if not command.document_id:
            raise ValueError("L'ID du document est requis")
        # tu peux ajouter d’autres validations ici
        return DocumentService.update_document(command.document_id, command.fields_to_update)
