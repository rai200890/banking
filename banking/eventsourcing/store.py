# encoding: utf-8
from .models import Subscriber, Event
from .models import db


def notify_by_email(email):
    pass


class EventStore(object):

    def __init__(self, entity_type):
        self.entity_type = entity_type

    def get_events(self, entity_id):
        return Event.query.filter_by(entity_type_id=self.entity_type.id,
                                     entity_id=entity_id).all()

    @classmethod
    def publish(cls, event):
        db.session.add(event)
        db.commit()
        subscribers = Subscriber.query.\
            find_by(event_type_id=event.event_type.id).all()
        for subscriber in subscribers:
            notify_by_email(subscriber.email)

    @classmethod
    def subscribe(cls, subscriber):
        db.session.add(subscriber)
        db.commit()

    @classmethod
    def unsubscribe(cls, subscriber_id):
        db.query.filter_by(id=subscriber_id).delete()
        db.commit()
