from flask.views import MethodView

from ..eventsourcing.repository import AccountRepository
from ..services.event import EventCommand
from ..app import event_store


class AccountResource(MethodView):

    def post(self, client_id):
        event = EventCommand.build(event_type="account",
                                   event_name="create_account")
        repository = AccountRepository(event_store=event_store)
        entity = repository.handle_event(event)
        return {"account": {}}

    def get(self, id):
        repository = AccountRepository(event_store=event_store)
        repository.get_entity(id)
