from ..app import db


class EventType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, index=True)
    entity = db.Column(db.String(80), unique=True, nullable=False, index=True)
    events = db.relationship("Events", back_populates="event_type")


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, nullable=False)
    version = db.Column(db.Integer, nullable=False, index=True, default=0)
    parameters = db.Column(db.JSON, nullable=False)
    event_type_id = db.Column(db.Integer, db.ForeignKey("event_type.id"), nullable=False)
