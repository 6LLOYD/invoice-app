from config import create_app, db
from controllers.document_controller import document_bp

app = create_app()

# Importer les modèles après la création de l'application
from models.adresse import Adresse
from models.client import Client
from models.document import Document
from models.item import Item
from models.profile import Profile
from models.service import Service

app.register_blueprint(document_bp, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)