from ..app import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, index=True)
    type = db.Column(db.String(80), unique=True, nullable=False, index=True)
    version = db.Column(db.Integer, nullable=False, index=True)
    parameters = db.Column(db.JSON, nullable=False, index=True)
    __mapper_args__ = {
        "polymorphic_identity": "event",
        "polymorphic_on": type
    }

class AccountEvent(db.Model):
    __tablename__ = "account_event"
    id = db.Column(Integer, db.ForeignKey("event.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "event"
    }


class TransferEvent(db.Model):
    __tablename__ = "transfer_event"
    id = db.Column(Integer, db.ForeignKey("event.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "event"
    }
