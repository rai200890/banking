from ..app import db
from ..models import Account


class GenericMutator(object):

    def __init__(self, entity_type, entity_id=None):
        self.entity_id = entity_id
        self.entity_type = entity_type

    def apply(self):
        pass


class AccountMutator(GenericMutator):
    def __init__(self, entity_type=Account, entity_id=None):
        super(AccountMutator, self).__init__(self, entity_type, entity_id)

    def apply(self):
        if self.event.event_type.name == "CreateAccount":
            entity = self.entity_type()
            entity.initial_balance = self.event.parameters.initial_balance
            entity.password = self.event.parameters.password

        # TODO: Não sei se faz sentido persistir a versão na entidade
        entity.version += 1
        db.session.add(entity)
        db.session.commit()

        return entity
