from ..app import db
from ..models import Account


class AccountQuery(object):

    @classmethod
    def find_by_id(cls, id):
        return Account.query.get(id)


class AccountCommand(object):

    @classmethod
    def create(cls, account=None, params={}):
        entity = Account(**params)
        db.session.add(entity)
        db.commit()

    @classmethod
    def withdraw(cls, account, params):
        pass

    @classmethod
    def deposit(cls, account, params):
        pass
