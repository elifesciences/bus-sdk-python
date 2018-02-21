from typing import NamedTuple

from elife_bus_sdk.queues import SQSMessageQueue


def test_can_get_queue(sqs_message_queue: SQSMessageQueue):
    assert sqs_message_queue.queue


def test_can_parse_message(sqs_message: NamedTuple,
                           sqs_message_queue: SQSMessageQueue):
    assert sqs_message_queue.parse_message(sqs_message)


def test_can_send_message(sqs_message_queue: SQSMessageQueue):
    assert sqs_message_queue.enqueue('test')


def test_can_receive_message(sqs_message_queue: SQSMessageQueue):
    assert sqs_message_queue.dequeue()


def test_can_poll_for_messages(sqs_message_queue: SQSMessageQueue):
    assert next(sqs_message_queue.poll())
