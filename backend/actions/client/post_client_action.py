from commands.client.post_client_command import PostClientCommand
from services.client_service import ClientService

class PostClientAction:
    @staticmethod
    def execute(command: PostClientCommand):
        if not command.nom or not command.prenom :
            raise ValueError("Nom et prenom sont requis")
        
        return ClientService.post_client(command)