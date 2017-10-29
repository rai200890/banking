from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from flasgger import Swagger


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config("SQLALCHEMY_TRACK_MODIFICATIONS", cast=bool, default=False)
    app.config["DEBUG"] = config("DEBUG", cast=bool, default=True)
    app.config["SWAGGER"] = {
        "title": "Banking API",
        "uiversion": 3,
        "specs_route": "/api/docs/"
    }
    db.init_app(app)
    from .api.blueprint import api
    app.register_blueprint(api)
    Swagger(app)
    return app
