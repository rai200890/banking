# encoding: utf-8
from functools import reduce


class Repository(object):

    def __init__(self, entity_type, event_store, mutator):
        self.event_store = event_store
        self.mutator = mutator
        self.entity_type = entity_type

    def handle_event(self, event, entity_id):
        self.event_store.publish(event)
        self.mutator.apply(event, entity_id)

    def get_entity(self, entity_id):
        entity = self.entity_type.find_by(id=entity_id).first()
        events = self.event_store.get_events(entity.id)
        return reduce(lambda entity, event: self.mutator.apply(event, entity.id),
                      events, entity)
