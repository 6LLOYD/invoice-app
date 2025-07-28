from services.document_service import DocumentService

class GetDocumentAction:
    @staticmethod
    def execute(command):
        return DocumentService.get_document(command.document_id)
