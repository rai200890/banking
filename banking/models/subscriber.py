from sqlalchemy_utils import EmailType

from ..app import db


class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(EmailType, nullable=False, index=True)
    event_type_id = db.Column(db.Integer, db.ForeignKey("event_type.id"), nullable=False)
    event_type = db.relationship("EventType", back_populates="events")
