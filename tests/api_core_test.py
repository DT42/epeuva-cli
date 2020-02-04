import unittest
from unittest import mock

import requests
import requests_mock

from epeuva_cli.api.core import create_login_token, get, post, put, patch, delete
from epeuva_cli.utils.config import config


class TestApiCore(unittest.TestCase):

    @requests_mock.Mocker()
    def test_create_login_token_created(self, mocker):
        mock_response = {
            'auth_token': 'abcdefgh1234567890',
        }
        mocker.register_uri(
            'POST',
            config.url + '/auth/login/',
            status_code=200,
            json=mock_response,
        )
        response = create_login_token()
        self.assertIn('auth_token', response)
        self.assertIsInstance(response['auth_token'], str)
        self.assertTrue(len(response['auth_token'])>1)

    @requests_mock.Mocker()
    def test_create_login_token_not_created(self, mocker):
        mock_response = {}
        mocker.register_uri(
            'POST',
            config.url + '/auth/login/',
            status_code=200,
            json=mock_response,
        )
        self.assertRaises(Exception, create_login_token)
