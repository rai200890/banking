from flask_migrate import Migrate

from .app import create_app, db
from .models import EventType

app = create_app()
Migrate(app, db)


@app.cli.command()
def seed():
    EventType.create(name="CreateAccount", entity="Client")
    EventType.create(name="WithdrawMoney", entity="Account")
    EventType.create(name="DepositMoney", entity="Account")
