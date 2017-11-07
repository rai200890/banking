from flask.views import MethodView
from flask import jsonify

from ..eventsourcing.repository import AccountRepository


# TODO: Code should be in services 
def get_account_ids(client_id):
    pass


class ClientResource(MethodView):

    def get(self, client_id):
        account_ids = get_account_ids(client_id)
        repository = AccountRepository()
        accounts = [repository.get_entity(account_id) for account_id in account_ids]
        return jsonify({
            "account": {
                "id": entity.id,
                "agency_id": entity.agency_id,
                "client_id": entity.client_id,
                "balance": 0
            }
        }), 200
