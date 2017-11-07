import logging
from logging.config import fileConfig
from os import getcwd

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from flasgger import Swagger

db = SQLAlchemy()

logger = logging.getLogger()


def handle_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


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
