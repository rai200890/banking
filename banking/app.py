from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config

from api.healthcheck import HealthcheckResource
from api.accounts import AccountResource
from api.clients import ClientResource
from api.subscriptions import SubscriptionResource
from api.transactions import TransactionResource


db = SQLAlchemy()


def mount_routes(app):
    app.add_url_rule("/api/healthcheck",
                 view_func=HealthcheckResource.as_view("healthcheck"),
                 methods=["GET"])
    app.add_url_rule("/api/accounts",
                     view_func=AccountResource.as_view("accounts"),
                     methods=["POST"])
    app.add_url_rule("/api/accounts/<account_id:int>/transactions",
                     view_func=TransactionResource.as_view("transactions"),
                     methods=["GET", "POST"])
    app.add_url_rule("/api/clients",
                     view_func=ClientResource.as_view("clients"),
                     methods=["GET", "POST"])
    app.add_url_rule("/api/clients/<client_id:int>/accounts",
                     view_func=AccountResource.as_view("accounts"),
                     methods=["GET"])
    app.add_url_rule("/api/subscriptions",
                     view_func=SubscriptionResource.as_view("subscriptions"),
                     methods=["POST"])
    app.add_url_rule("/api/subscriptions/<subscription_id:int>",
                     view_func=TransactionResource.as_view("subscriptions"),
                     methods=["DELETE"])
    app.add_url_rule("/api/accounts/<account_id:int>/transactions",
                     view_func=TransactionResource.as_view("transactions"),
                     methods=["GET", "POST"])

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config("SQLALCHEMY_TRACK_MODIFICATIONS", cast=bool, default=False)
    app.config["DEBUG"] = config("DEBUG", cast=bool, default=True)
    db.init_app(app)
    mount_routes(app)

    return app
