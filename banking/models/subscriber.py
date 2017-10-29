from sqlalchemy_utils import EmailType

from ..app import db


class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(EmailType, nullable=False, index=True)
