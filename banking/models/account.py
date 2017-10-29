from sqlalchemy_utils import PasswordType, CurrencyType

from ..app import db


class Agency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, index=True)
    number = db.Column(db.String(20), unique=True, index=True)
    accounts = db.relationship("Account", back_populates="agency")


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(40), unique=True, index=True)
    password = db.Column(PasswordType, nullable=False, index=True)
    initial_balance = db.Column(CurrencyType, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False, index=True)
    agency_id = db.Column(db.Integer, db.ForeignKey("agency.id"), nullable=False, index=True)
