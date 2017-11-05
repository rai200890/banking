from flask.views import MethodView
from webargs.flaskparser import use_kwargs

from ..eventsourcing.repository import AccountRepository
from ..services.event import EventCommand
from ..app import event_store
from ..schemas.account import AccountSchema


class AccountResource(MethodView):

    @use_kwargs(AccountSchema(strict=True))
    def post(self, client_id):
        event = EventCommand.build(event_type="account",
                                   event_name="create_account")
        repository = AccountRepository(event_store=event_store)
        entity = repository.handle_event(event)
        return {
            "account": {
                "id": entity.id,
                "agency_id": entity.agency_id,
                "client_id": entity.client_id
            }
        }

    def get(self, id):
        repository = AccountRepository(event_store=event_store)
        repository.get_entity(id)
