# encoding: utf-8
from ..services.event import EventQuery
from ..services.subscriber import (
    SubscriberQuery,
    SubscriberEventCommand
)
from ..app import db


def notify_by_email(email):
    pass


class EventStore(object):

    def __init__(self, entity_name):
        self.entity_name = entity_name

    def get_events(self, entity_id):
        return EventQuery.filter_by(entity_name=self.entity_name,
                                    entity_id=entity_id)

    def get_subscribers(self, event):
        return SubscriberQuery.filter_by(event_name=event.event_type.name,
                                         entity_name=self.entity_name)

    def publish(self, event):
        db.session.add(event)
        db.session.commit()
        for subscriber in self.get_subscribers(event):
            notify_by_email(subscriber.email)

    def subscribe(self, event_name, subscriber_id):
        return SubscriberEventCommand.create(event_name=event_name,
                                             subscriber_id=subscriber_id,
                                             entity_name=self.entity_name)

    def unsubscribe(self, subscriber_id, event_name):
        return SubscriberEventCommand.delete(event_name=event_name,
                                             entity_name=self.entity_name,
                                             subscriber_id=subscriber_id)
