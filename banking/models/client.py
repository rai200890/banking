from sqlalchemy_utils.types.phone_number import PhoneNumber


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, index=True)
    accounts = db.relationship("Account", back_populates="client")
