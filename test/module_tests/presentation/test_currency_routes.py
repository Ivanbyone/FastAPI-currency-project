""" """

from test.module_tests.presentation.client import test_client


def test_exchange():
    """ """
    response = test_client.post(url='/currency/exchange')

    assert response.status_code == 201


def test_list():
    """ """
    response = test_client.get(url='/currency/list/')

    assert response.status_code == 200
