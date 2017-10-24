from ..app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity = db.Column(db.String(80), unique=True, nullable=False)
    parameters = db.Column(db.JSON, nullable=False)
