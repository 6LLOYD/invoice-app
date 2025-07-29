class PostClientCommand:
    def __init__(self,nom, prenom, email=None, telephone=None, adresse_id=None):

        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
        self.adresse_id = adresse_id