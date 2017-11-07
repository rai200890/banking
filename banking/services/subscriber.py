from ..app import db
from ..models import Subscriber, SubscriberEvent, EventType
from .event import EventTypeQuery


class SubscriberQuery(object):

    @classmethod
    def filter_by(cls, event_name, entity_name, subscriber_id=None):
        query = Subscriber.query.join(SubscriberEvent).join(EventType).\
            filter(EventType.name == event_name,
                   EventType.entity == entity_name)

        if subscriber_id:
            return query.filter_by(id=subscriber_id)

        return query


class SubscriberEventQuery(object):

    @classmethod
    def filter_by(cls, event_name, entity_name, subscriber_id):
        return SubscriberEvent.query.join(EventType).\
            filter(SubscriberEvent.subscriber_id == subscriber_id,
                   EventType.name == event_name,
                   EventType.entity == entity_name)


class SubscriberEventCommand(object):

    @classmethod
    def create(cls, event_name, entity_name, subscriber_id):
        event_type = EventTypeQuery.get_by(event_name=event_name,
                                           entity_name=entity_name)
        subscriber_event = SubscriberEvent(subscriber_id=subscriber_id,
                                           event_type_id=event_type.id)
        db.session.add(subscriber_event)
        db.session.commit()
        return subscriber_event

    @classmethod
    def delete(cls, event_name, entity_name, subscriber_id):
        return SubscriberEventQuery.filter_by(event_name=event_name,
                                              entity_name=entity_name,
                                              subscriber_id=subscriber_id).delete()
