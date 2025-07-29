class PostDocumentCommand:
    def __init__(
        self, numero, date, total_ht, tva_taux=5.5, tva_montant=None, total_ttc=None,
        type_document=None, client_id=None, profile_id=None,
        statut='Brouillon', adresse_chantier=None,
        nom_client=None, email_client=None, telephone_client=None, adresse_client=None,
        document_source_id=None
    ):
        self.numero = numero
        self.date = date
        self.total_ht = total_ht
        self.tva_taux = tva_taux
        self.tva_montant = tva_montant
        self.total_ttc = total_ttc
        self.type_document = type_document
        self.client_id = client_id
        self.profile_id = profile_id
        self.statut = statut
        self.adresse_chantier = adresse_chantier
        self.nom_client = nom_client
        self.email_client = email_client
        self.telephone_client = telephone_client
        self.adresse_client = adresse_client
        self.document_source_id = document_source_id
