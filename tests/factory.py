import factory

from banking.app import db
from banking.models import Account, EventType, Event, Subscriber, SubscriberEvent


class AccountFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Account
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    password = factory.Faker("word")


class EventTypeFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = EventType
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    entity = factory.Sequence(lambda n: "Entity{}".format(n))
    name = factory.Sequence(lambda n: "event_name{}".format(n))

    class Params:
        create = factory.Trait(
            name="create",
            entity="Account"
        )
        deposit = factory.Trait(
            name="deposit",
            entity="Account"
        )
        withdraw = factory.Trait(
            name="withdraw",
            entity="Account"
        )


class EventFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Event
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    version = factory.Sequence(lambda n: n)
    entity_id = factory.Sequence(lambda n: n)
    params = {}
    event_type = factory.SubFactory(EventTypeFactory)


class SubscriberFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Subscriber
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    email = factory.Faker("email")


class SubscriberEventFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = SubscriberEvent
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    subscriber = factory.SubFactory(SubscriberFactory)
    event_type = factory.SubFactory(EventTypeFactory)
