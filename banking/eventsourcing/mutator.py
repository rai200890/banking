from ..app import logger
from ..services.account import AccountCommand


class AccountMutator(object):

    SUPPORTED_ACTIONS = ["create", "deposit", "withdraw"]

    @classmethod
    def apply(cls, event, entity):
        event_name = event.event_type.name
        try:
            if event_name in cls.SUPPORTED_EVENTS:
                action = getattr(AccountCommand, event_name)
                entity = action(entity=entity, params=event.parameters)
                return entity
            raise Exception("Unsupported event {} for account".format(event_name))
        except Exception as e:
            logger.error(e)
