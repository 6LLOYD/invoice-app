class PostDocumentCommand:
    def __init__(self, numero, date, total, type_document, client_id, profile_id=None):
        self.numero = numero
        self.date = date
        self.total = total
        self.type_document = type_document
        self.client_id = client_id
        self.profile_id = profile_id