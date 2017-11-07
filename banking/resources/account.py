from flask.views import MethodView
from flask import jsonify
from webargs.flaskparser import use_kwargs

from ..eventsourcing.repository import AccountRepository
from ..services.event import EventFactory
from ..schemas.account import AccountSchema


class AccountResource(MethodView):

    @use_kwargs(AccountSchema(strict=True))
    def post(self, client_id):
        event = EventFactory(entity_name="Account",
                             event_name="create").build()
        repository = AccountRepository()
        entity = repository.handle_event(event)
        return (jsonify({
            "account": {
                "id": entity.id,
                "agency_id": entity.agency_id,
                "client_id": entity.client_id,
                "balance": entity.initial_balance,
                "transactions": []
            }
        }), 201)
