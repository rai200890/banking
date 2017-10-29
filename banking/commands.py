from flask_migrate import Migrate

from .app import create_app, db
from .models import EventType

app = create_app()
Migrate(app, db)


@app.cli.command()
def seed():
    db.session.add(EventType(name="CreateAccount", entity="Client"))
    db.session.add(EventType(name="WithdrawMoney", entity="Account"))
    db.session.add(EventType(name="DepositMoney", entity="Account"))
    db.session.commit()
