import unittest
from unittest import mock

import requests
import requests_mock

from epeuva_cli.api import apps
from epeuva_cli.utils.config import config


class TestApiApps(unittest.TestCase):

    @requests_mock.Mocker()
    def test_apps_get_list(self, mocker):
        mock_response = [
            {
                'cover': 'mock-cover.jpg',
                'description': '',
                'groups': [
                    1
                ],
                'id': 1,
                'name': 'mock-app',
            }
        ]
        mocker.register_uri(
            'GET',
            config.url + '/apps',
            status_code=200,
            json=mock_response,
        )
        response = apps.get_list()
        self.assertIsInstance(response, list)


    @requests_mock.Mocker()
    def test_apps_get_detail(self, mocker):
        mock_response = {
            'cover': 'mock-cover.jpg',
            'descrption': '',
            'groups': [
                1
            ],
            'id': 1,
            'name': 'mock-app',
        }
        mocker.register_uri(
            'GET',
            config.url + '/apps/1',
            status_code=200,
            json=mock_response,
        )
        response = apps.get_detail(1)
        self.assertIsInstance(response, dict)
