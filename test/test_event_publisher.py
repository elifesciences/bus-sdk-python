from bus_sdk import get_publisher
from bus_sdk.publishers import SNSPublisher


def test_it_will_receive_default_name_if_name_is_not_supplied(valid_config):
    publisher = get_publisher(pub_type='sns', config=valid_config)
    publisher2 = get_publisher(pub_name='default_publisher')
    assert publisher is publisher2


def test_it_will_receive_default_type_if_type_is_not_supplied(valid_config):
    publisher = get_publisher('test1', config=valid_config)
    assert isinstance(publisher, SNSPublisher)


def test_it_returns_an_event_publisher_instance_when_supplying_a_valid_type(valid_config):
    publisher = get_publisher('test1', pub_type='sns', config=valid_config)
    assert type(publisher) == SNSPublisher
