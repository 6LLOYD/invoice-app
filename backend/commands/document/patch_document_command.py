class PatchDocumentCommand:
    def __init__(self, document_id, fields_to_update: dict):
        self.document_id = document_id
        self.fields_to_update = fields_to_update
