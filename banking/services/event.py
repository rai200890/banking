from ..models import Event, EventType


class EventTypeQuery(object):

    @classmethod
    def find(cls, event_name, event_type):
        return EventType.query.find_by(event_name=event_name,
                                       entity=event_type)


class EventCommand(object):

    @classmethod
    def build(entity_type, event_name, parameters={}):
        event_type = EventTypeQuery.find(event_name=event_name,
                                         event_type=entity_type)
        return Event(event_type=event_type, parameters=parameters)
