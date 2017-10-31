import json


class Message(dict):
    """
    Subclass of the built in `dict` type which allows enforcement
    of required fields.
    """
    _type = 'base_msg'
    required_fields = []

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize as you would a normal `dict`.

        >>> data = {'id': 1234}
        >>> msg = Message(**data)
        >>> print(msg)
        {'id': 1234, 'type': 'base_msg'}"

        # or

        >>> msg = Message(id=1234)
        >>> print(msg)
        {'id': 1234, 'type': 'test_msg'}"

        :param args:
        :param kwargs:
        """
        kwargs['type'] = self._type
        super(Message, self).__init__(*args, **kwargs)

        for field in self.required_fields:
            if not self.get(field):
                raise AttributeError('{} is a required field'.format(field))

    def to_json(self):
        return json.dumps(self)


class ArticleMessage(Message):
    _type = 'article'
    required_fields = ['id']


class CollectionMessage(Message):
    _type = 'collection'
    required_fields = ['id']


class MetricMessage(Message):
    _type = 'metrics'
    required_fields = ['contentType', 'id', 'metric']


class PodcastEpisodeMessage(Message):
    _type = 'podcast-episode'
    required_fields = ['number']


class ProfileMessage(Message):
    _type = 'profile'
    required_fields = ['id']
