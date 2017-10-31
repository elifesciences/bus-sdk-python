import pytest

from bus_sdk import get_publisher
from bus_sdk.publishers import SNSPublisher


def test_it_raises_an_error_if_name_is_not_supplied(valid_config):
    with pytest.raises(TypeError):
        get_publisher(pub_type='sns', config=valid_config)


def test_it_raises_an_error_if_type_is_not_supplied_when_publisher_is_not_initialized(valid_config):
    with pytest.raises(AttributeError):
        get_publisher('test1', config=valid_config)


def test_it_returns_an_event_publisher_instance_when_supplying_a_valid_type(valid_config):
    publisher = get_publisher('test1', pub_type='sns', config=valid_config)
    assert type(publisher) == SNSPublisher
