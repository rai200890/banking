from banking.app import create_app
from banking.models import db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)
