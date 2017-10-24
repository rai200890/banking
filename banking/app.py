from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config("SQLALCHEMY_TRACK_MODIFICATIONS", cast=bool, default=False)
    app.config["DEBUG"] = config("DEBUG", cast=bool)
    from banking.models.event import Event
    db.init_app(app)

    @app.route("/")
    def hello():
        from banking.models.event import Event
        Event.query.all()
        return "Hello World!"

    return app
