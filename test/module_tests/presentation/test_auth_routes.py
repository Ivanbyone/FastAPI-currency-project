""" """

from test.module_tests.presentation.client import test_client


def test_register():
    """ """
    response = test_client.post(url='/auth/register')

    assert response.status_code == 201


def test_login():
    """ """
    response = test_client.post(url='/auth/login')

    assert response.status_code == 200
