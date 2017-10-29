from ..app import db
from .models import Account


class AccountCommand(object):

    @classmethod
    def create(cls, params={}):
        entity = Account(params)
        db.session.add(entity)
        db.commit()

    def update_version(cls, entity):
        pass


class AccountQuery(object):

    @classmethod
    def get_by_id(cls, id):
        pass
