from unittest.mock import patch

import pytest

from bus_sdk.messages import ProfileMessage
from bus_sdk.publishers import SNSPublisher


def test_it_will_create_arn_with_if_config_is_valid(dev_config_overrides, valid_config):
    publisher = SNSPublisher(**valid_config, **dev_config_overrides)
    assert publisher.arn == 'arn:aws:sns:local:00000000000:test-topic--dev'


def test_it_will_fail_to_publish_an_invalid_message(dev_config_overrides, valid_config):
    message = {'invlaid': 'data'}
    publisher = SNSPublisher(**valid_config, **dev_config_overrides)
    with pytest.raises(AttributeError):
        publisher.publish(message=message)


@patch('bus_sdk.publishers.sns_publisher.boto3')
def test_it_will_publish_a_valid_message(mock_boto, dev_config_overrides, valid_config):
    mock_boto.resource.Topic.publish.return_value = {}

    message = ProfileMessage(id='12345')
    publisher = SNSPublisher(**valid_config, **dev_config_overrides)
    assert publisher.publish(message=message)


def test_it_will_raise_error_if_passed_invalid_message_type(dev_config_overrides, valid_config):
    message = 'invalid_type'
    publisher = SNSPublisher(**valid_config, **dev_config_overrides)
    with pytest.raises(AttributeError):
        publisher.publish(message=message)
