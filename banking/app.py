import logging
from logging.config import fileConfig
from os import getcwd

from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from flasgger import Swagger
from werkzeug.local import LocalProxy

db = SQLAlchemy()

logger = logging.getLogger()


def get_event_store():
    from .eventsourcing.store import EventStore
    event_store = getattr(g, "_event_store", None)
    if event_store is None:
        event_store = g._event_store = EventStore()


event_store = LocalProxy(get_event_store)


def create_app():
    fileConfig(config("LOG_CONFIG",
               default="{}/banking/conf/logging.default.cfg".format(getcwd())))
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config("SQLALCHEMY_TRACK_MODIFICATIONS",
                                                          cast=bool,
                                                          default=False)
    app.config["DEBUG"] = config("DEBUG", cast=bool, default=True)
    app.config["SWAGGER"] = {
        "title": "Banking API",
        "uiversion": 3,
        "specs_route": "/api/docs/"
    }
    db.init_app(app)
    from .resources import blueprint
    app.register_blueprint(blueprint)
    Swagger(app)
    return app
