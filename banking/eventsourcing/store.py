# encoding: utf-8
from .models import Subscriber, Event, EventType
from .models import db


def notify_by_email(email):
    pass


class EventStore(object):

    def get_events(self, entity_type, entity_id):
        return Event.query.filter(EventType.name == entity_type,
                                  Event.entity_id == entity_id).all()

    def publish(self, event):
        db.session.add(event)
        db.commit()
        subscribers = Subscriber.query.\
            find_by(event_type_id=event.event_type.id).all()
        for subscriber in subscribers:
            notify_by_email(subscriber.email)

    def subscribe(self, subscriber):
        db.session.add(subscriber)
        db.commit()

    @classmethod
    def unsubscribe(self, subscriber_id):
        db.query.filter_by(id=subscriber_id).delete()
        db.commit()
