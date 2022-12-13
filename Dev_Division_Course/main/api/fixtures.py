import pytest

from api.client import ApiClient

@pytest.fixture(scope='session')
def cookies(api_client):
    return api_client.session.cookies


@pytest.fixture(scope='session')
def api_client(base_url, user):
    client = ApiClient(base_url)
    client.post_user_auth(user.EMAIL, user.PASSWORD)

    return client
