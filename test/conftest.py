from pytest import fixture


@fixture
def dev_config_overrides():
    return {
        'endpoint_url': 'http://0.0.0.0:4100'
    }


@fixture
def invalid_config():
    return {'invalid': 'config'}


@fixture
def valid_config():
    return {
        'region': 'local',
        'subscriber': '00000000000',
        'name': 'test-topic',
        'env': 'dev'
    }
