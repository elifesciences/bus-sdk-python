from typing import Dict, Generator, List

try:
    import boto3
except ImportError:  # pragma: no cover
    # boto3 not yet available, may happen in initial install of elife_bus_sdk package
    pass

from elife_bus_sdk.queues.message_queue import MessageQueue


class SQSMessageQueue(MessageQueue):
    name = 'sqs'

    def __init__(self, **overrides):
        self._queue_name = overrides.pop('QueueName', None)
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
    def parse_message(message: 'sqs.Message') -> Dict[str, str]:
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

    def poll(self, parse_msg: bool = True) -> Generator[Dict, None, None]:
        """An infinite poll on the given queue object.

        Blocks for `WaitTimeSeconds` seconds before connection is dropped and re-established.

        If `parse_msg` is False, then you will be returned the the original `sqs.Message` object.

        :param parse_msg: bool
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
                if parse_msg:
                    yield self.parse_message(message)
                else:
                    yield message
            except AttributeError:
                yield {}
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
