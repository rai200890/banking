from flask_migrate import Migrate

from .app import create_app, db
from .models import EventType

app = create_app()
Migrate(app, db)


@app.cli.command()
def seed():
    db.session.add(EventType(name="create", entity="account"))
    db.session.add(EventType(name="withdraw", entity="account"))
    db.session.add(EventType(name="deposit", entity="account"))
    db.session.commit()
