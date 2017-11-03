from flask import Blueprint

from .healthcheck import HealthcheckResource
from .accounts import AccountResource
from .subscriptions import SubscriptionResource
from .transactions import TransactionResource


api = Blueprint("API", "api")


api.add_url_rule("/api/healthcheck",
                 view_func=HealthcheckResource.as_view("healthcheck"),
                 methods=["GET"])
api.add_url_rule("/api/accounts",
                 view_func=AccountResource.as_view("post_accounts"),
                 methods=["POST"])
api.add_url_rule("/api/accounts/<account_id>/transactions",
                 view_func=TransactionResource.as_view("transactions"),
                 methods=["GET", "POST"])
api.add_url_rule("/api/accounts",
                 view_func=AccountResource.as_view("get_accounts"),
                 methods=["GET"])
api.add_url_rule("/api/subscriptions",
                 view_func=SubscriptionResource.as_view("post_subscriptions"),
                 methods=["POST"])
api.add_url_rule("/api/subscriptions/<subscription_id>",
                 view_func=TransactionResource.as_view("delete_subscriptions"),
                 methods=["DELETE"])
