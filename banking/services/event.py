from ..models import Event, EventType


class EventTypeQuery(object):

    @classmethod
    def get_by(cls, event_name, event_type):
        return EventType.query.find_by(event_name=event_name,
                                       entity=event_type).first()


class EventQuery(object):

    @classmethod
    def filter_by(cls, entity_type, entity_id):
        return Event.query.filter(EventType.name == entity_type,
                                  Event.entity_id == entity_id).all()


class EventFactory(object):

    def __init__(self, event_name, entity_name, parameters={}):
        self.event_name = event_name
        self.entity_name = entity_name
        self.parameters = parameters

    @property
    def event_type(self):
        return EventTypeQuery.get_by(event_name=self.event_name,
                                     entity_name=self.entity_name)

    def build(self):
        return Event(event_type=self.event_type,
                     parameters=self.parameters)
