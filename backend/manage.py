from flask.cli import FlaskGroup
from config import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

from models.adresse import Adresse
from models.client import Client
from models.document import Document
from models.item import Item
from models.profile import Profile
from models.service import Service

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()
