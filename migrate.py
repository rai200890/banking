from banking.app import create_app, db
from banking import models
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)
