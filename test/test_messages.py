import pytest

from bus_sdk.messages import (
    ArticleMessage,
    CollectionMessage,
    MetricMessage,
    PodcastEpisodeMessage,
    ProfileMessage
)


@pytest.mark.parametrize('message_class', [
    ArticleMessage,
    CollectionMessage,
    ProfileMessage
])
def test_message_will_init_with_required_fields_populated(message_class):
    assert message_class(id='12345')


@pytest.mark.parametrize('message_class', [
    ArticleMessage,
    CollectionMessage,
    ProfileMessage
])
def test_message_will_raise_exception_without_required_fields(message_class):
    with pytest.raises(AttributeError):
        message_class()


@pytest.mark.parametrize('message_class', [
    ArticleMessage,
    CollectionMessage,
    ProfileMessage
])
def test_message_can_be_converted_to_json(message_class):
    msg = message_class(id='12345')

    assert isinstance(msg.to_json(), str)


@pytest.mark.parametrize('message_class', [
    ArticleMessage,
    CollectionMessage,
    ProfileMessage
])
def test_it_will_allow_additional_fields_on_init(message_class):
    valid_data = {
        'id': 1234,
        'event': 'user_updated'
    }
    msg = message_class(**valid_data)

    assert msg['event'] == 'user_updated'


def test_metric_message_will_init_with_required_fields_populated():
    assert MetricMessage(contentType='someType', id='1234', metric='someMetric')


def test_metric_message_will_raise_exception_without_required_fields():
    with pytest.raises(AttributeError):
        MetricMessage()


def test_metric_message_can_be_converted_to_json():
    msg = MetricMessage(contentType='someType', id='1234', metric='someMetric')

    assert isinstance(msg.to_json(), str)


def test_metric_message_will_allow_additional_fields_on_init():
    valid_data = {
        'contentType': 'someType',
        'id': 1234,
        'metric': 'someMetric',
        'event': 'user_updated'
    }
    msg = MetricMessage(**valid_data)

    assert msg['event'] == 'user_updated'


def test_podcast_message_will_init_with_required_fields_populated():
    assert PodcastEpisodeMessage(number=1234)


def test_podcast_message_will_raise_exception_without_required_fields():
    with pytest.raises(AttributeError):
        PodcastEpisodeMessage()


def test_podcast_message_can_be_converted_to_json():
    msg = PodcastEpisodeMessage(number=1234)

    assert isinstance(msg.to_json(), str)


def test_podcast_message_will_allow_additional_fields_on_init():
    valid_data = {
        'number': 1234,
        'event': 'user_updated'
    }
    msg = PodcastEpisodeMessage(**valid_data)

    assert msg['event'] == 'user_updated'
