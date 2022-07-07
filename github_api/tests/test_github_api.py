from unittest.mock import Mock

import pytest

from github_api import github_api

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = "https://avatars.githubusercontent.com/u/11700457?v=4"
    resp_mock.json.return_value = {'login': 'cassianoczz', 'id': 11700457, 'node_id': 'MDQ6VXNlcjExNzAwNDU3',
                                   'avatar_url': 'https://avatars.githubusercontent.com/u/11700457?v=4'}
    get_mock = mocker.patch("github_api.github_api.requests.get")
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar("cassianoczz")
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar("cassianoczz")
    assert "https://avatars.githubusercontent.com/u/11700457?v=4" == url
