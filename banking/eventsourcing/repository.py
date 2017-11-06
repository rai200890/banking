# encoding: utf-8
from functools import reduce

from .mutator import AccountMutator
from .store import EventStore
from ..services.account import AccountQuery


class AccountRepository(object):

    def __init__(self):
        self.event_store = EventStore("Account")
        self.mutator = AccountMutator()

    def handle_event(self, event, entity_id=None):
        self.event_store.publish(event)
        entity = self.get_entity(entity_id) if entity_id else None
        self.mutator.apply(event=event, entity=entity)

    def get_entity(self, entity_id):
        entity = AccountQuery.find_by_id(entity_id)
        events = self.event_store.get_events(entity.id)
        return reduce(lambda entity, event: self.mutator.apply(event, entity.id),
                      events, entity)
