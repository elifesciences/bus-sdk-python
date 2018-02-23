from collections import namedtuple
from unittest.mock import patch, MagicMock
from typing import Dict, NamedTuple

from pytest import fixture

from elife_bus_sdk.publishers import SNSPublisher
from elife_bus_sdk.queues import SQSMessageQueue


@fixture
def dev_config_overrides() -> Dict[str, str]:
    return {
        'endpoint_url': 'http://0.0.0.0:4100'
    }


@fixture
def invalid_config() -> Dict[str, str]:
    return {'invalid': 'config'}


@fixture
def mock_sqs_queue(sqs_message: NamedTuple) -> MagicMock:
    mock_queue = MagicMock()
    mock_queue.receive_messages.return_value = [sqs_message]
    return mock_queue


@fixture
def sqs_message() -> NamedTuple:
    fields = ['body',
              'md5_of_body',
              'message_id',
              'queue_url',
              'receipt_handle']

    message = namedtuple('Message', fields)

    return message(
        body='body',
        md5_of_body='md5 body',
        message_id='0000000',
        queue_url='some url',
        receipt_handle='111111',
    )


@fixture
@patch('elife_bus_sdk.publishers.sns_publisher.boto3')
# pylint:disable=unused-argument
def sns_publisher(mock_boto: MagicMock, dev_config_overrides: Dict[str, str],
                  valid_config: Dict[str, str]):
    return SNSPublisher(**valid_config, **dev_config_overrides)


@fixture
@patch('elife_bus_sdk.queues.sqs_queue.boto3')
# pylint:disable=unused-argument
def sqs_message_queue(mock_boto: MagicMock, mock_sqs_queue,
                      valid_sqs_config: Dict[str, str]):
    mock_boto.resource.return_value.get_queue_by_name.return_value = mock_sqs_queue
    return SQSMessageQueue(**valid_sqs_config)


@fixture
def valid_config() -> Dict[str, str]:
    return {
        'region': 'local',
        'subscriber': '00000000000',
        'name': 'test-topic',
        'env': 'dev'
    }


@fixture
def valid_sqs_config() -> Dict[str, str]:
    return {
        'queue_name': 'test7',
    }
