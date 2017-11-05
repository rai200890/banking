from sqlalchemy.orm import column_property
from sqlalchemy_utils import PasswordType, CurrencyType

from ..app import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(PasswordType(
        schemes=[
            "pbkdf2_sha512",
            "md5_crypt"
        ],
        deprecated=["md5_crypt"]
    ), nullable=False, index=True)
    version = db.Column(db.Integer, default=0, nullable=False)
    initial_balance = db.Column(CurrencyType, nullable=False)
    client_id = db.Column(db.Integer, nullable=False)
    agency_id = db.Column(db.Integer, nullable=False)
    # number = column_property(user_table.c.id, address_table.c.user_id)
