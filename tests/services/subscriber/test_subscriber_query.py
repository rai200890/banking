import pytest

from tests import factory
from banking.services.subscriber import SubscriberQuery


@pytest.fixture
def event_type_create():
    return factory.EventTypeFactory.create(create=True)


@pytest.fixture
def event_type_deposit():
    return factory.EventTypeFactory.create(deposit=True)


@pytest.fixture
def event_type_withdraw():
    return factory.EventTypeFactory.create(withdraw=True)


@pytest.fixture
def subscriber_of_create_and_deposit(event_type_create, event_type_deposit):
    subscriber = factory.SubscriberFactory.create()
    factory.SubscriberEvent(subscriber=subscriber, event_type=event_type_create)
    factory.SubscriberEvent(subscriber=subscriber, event_type=event_type_deposit)
    return subscriber


@pytest.fixture
def subscriber_of_deposit(event_type_deposit):
    subscriber = factory.SubscriberFactory.create()
    factory.SubscriberEvent(subscriber=subscriber, event_type=event_type_deposit)
    return subscriber


@pytest.fixture
def subscriber_of_withdraw(event_type_withdraw):
    subscriber = factory.SubscriberFactory.create()
    factory.SubscriberEvent(subscriber=subscriber, event_type=event_type_withdraw)
    return subscriber


def test_filter_by_without_subscriber_id(subscriber_of_withdraw,
                                         subscriber_of_create_and_deposit,
                                         subscriber_of_deposit):

    query = SubscriberQuery.filter_by(event_name="deposit", entity_name="Account")

    assert subscriber_of_deposit in query.all()
    assert subscriber_of_create_and_deposit in query.all()
    assert query.count() == 2


def test_filter_by_with_subscriber_id(subscriber_of_withdraw,
                                      subscriber_of_create_and_deposit,
                                      subscriber_of_deposit):

    query = SubscriberQuery.filter_by(event_name="create", entity_name="Account",
                                      subscriber_id=subscriber_of_create_and_deposit.id)

    assert query.all() == [subscriber_of_create_and_deposit]
