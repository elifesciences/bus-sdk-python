from typing import Dict, Generator, List

import boto3

from elife_bus_sdk.events import Event
from elife_bus_sdk.queues.message_queue import MessageQueue


class SQSMessageQueue(MessageQueue):
    name = 'sqs'

    def __init__(self, **overrides):
        self._queue_name = overrides.pop('queue_name', None)
        self._overrides = overrides
        self._resource = boto3.resource(self.name, **self._overrides)
        self._queue = self._resource.get_queue_by_name(QueueName=self._queue_name)

    def dequeue(self) -> List['sqs.Message']:
        """Retrieves one or more messages (up to 10), from the queue.

        :return: list
        """
        conf = self._overrides
        return self._queue.receive_messages(MaxNumberOfMessages=conf.get('MaxNumberOfMessages', 1),
                                            VisibilityTimeout=conf.get('VisibilityTimeout', 60),
                                            WaitTimeSeconds=conf.get('WaitTimeSeconds', 20))

    def enqueue(self, message: str) -> Dict[str, str]:
        """Delivers a message to the queue.

        :param message: str
        :return: dict

        example return value:
        {
            'MD5OfMessageBody': 'string',
            'MD5OfMessageAttributes': 'string',
            'MessageId': 'string',
            'SequenceNumber': 'string'
        }
        """
        return self._queue.send_message(MessageBody=message)

    @staticmethod
    def _parse_message(message: 'sqs.Message') -> Dict[str, str]:
        """Parse a `sqs.Message` object and return a `dict` representation.

        :param message: :class: sqs.Message
        :return: dict
        """
        return {
            'body': message.body,
            'md5_of_body': message.md5_of_body,
            'message_id': message.message_id,
            'queue_url': message.queue_url,
            'receipt_handle': message.receipt_handle
        }

    def poll(self) -> Generator[Event, None, None]:
        """An infinite poll on the given queue object.

        Blocks for `WaitTimeSeconds` seconds before connection is dropped and re-established.

        :return: generator
        """
        while True:
            messages = []

            while not messages:
                messages = self.dequeue()

            if not messages:
                continue

            message = messages[0]

            try:
                yield Event(**self._parse_message(message))
            except AttributeError:
                yield None
            finally:
                message.delete()

    @property
    def queue(self) -> 'sqs.Queue':
        """Returns the current `sqs.Queue` instance for the class.

        Any additional `boto3.sqs.Queue` functionality can be accessed by using this
        object directly.

        :return: :class: `sqs.Queue`
        """
        return self._queue
