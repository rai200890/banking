from flask import Blueprint

from .healthcheck import HealthcheckResource
from .account import AccountResource
from .subscription import SubscriptionResource
from .transaction import TransactionResource


blueprint = Blueprint("API", "api")


blueprint.add_url_rule("/api/healthcheck",
                       view_func=HealthcheckResource.as_view("healthcheck"),
                       methods=["GET"])
blueprint.add_url_rule("/api/accounts",
                       view_func=AccountResource.as_view("post_accounts"),
                       methods=["POST"])
blueprint.add_url_rule("/api/accounts/<account_id>/transactions",
                       view_func=TransactionResource.as_view("transactions"),
                       methods=["GET", "POST"])
blueprint.add_url_rule("/api/accounts",
                       view_func=AccountResource.as_view("get_accounts"),
                       methods=["GET"])
blueprint.add_url_rule("/api/subscriptions",
                       view_func=SubscriptionResource.as_view("post_subscriptions"),
                       methods=["POST"])
blueprint.add_url_rule("/api/subscriptions/<subscription_id>",
                       view_func=TransactionResource.as_view("delete_subscriptions"),
                       methods=["DELETE"])
