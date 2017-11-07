from sqlalchemy_utils import EmailType

from ..app import db


class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(EmailType, nullable=False, index=True)
    event_types = db.relationship("SubscriberEvent",
                                  back_populates="subscriber")


class SubscriberEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subscriber_id = db.Column(db.Integer, db.ForeignKey("subscriber.id"),
                              nullable=False)
    event_type_id = db.Column(db.Integer, db.ForeignKey("event_type.id"),
                              nullable=False)
    subscriber = db.relationship("Subscriber", back_populates="event_types")
    event_type = db.relationship("EventType", back_populates="subscribers")
