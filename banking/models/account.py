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
    password = db.Column(PasswordType(
        schemes=[
            "pbkdf2_sha512",
            "md5_crypt"
        ],
        deprecated=["md5_crypt"]
    ), nullable=False, index=True)
    version = db.Column(db.Integer, default=0)
    initial_balance = db.Column(CurrencyType, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    agency_id = db.Column(db.Integer, db.ForeignKey("agency.id"), nullable=False)
    client = db.relationship("Client", back_populates="accounts")
    agency = db.relationship("Agency", back_populates="accounts")
