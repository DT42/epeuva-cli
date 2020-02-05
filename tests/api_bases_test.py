import unittest
import uuid

import requests_mock

from epeuva_cli.api import bases
from epeuva_cli.utils.config import config


class TestApiBases(unittest.TestCase):

    def is_valid_uuid4(self, uuid_str):
        try:
            val = uuid.UUID(uuid_str, version=4)
        except Exception:
            return False
        return str(val) == uuid_str

    @requests_mock.Mocker()
    def test_bases_get_list(self, mocker):
        mock_response = [
            {
                'app': 1,
                'base_model_assets': '',
                'base_model_dir_path': '',
                'base_model_meta_path': '',
                'base_model_sha256sum': '',
                'id': 1,
                'name': 'mock-base-model',
            }
        ]
        mocker.register_uri(
            'GET',
            config.url + '/base_models?app=1',
            status_code=200,
            json=mock_response,
        )
        response = bases.get_list(1)
        self.assertIsInstance(response, list)

    @requests_mock.Mocker()
    def test_bases_get_detail(self, mocker):
        mock_response = {
            'app': 1,
            'base_model_assets': '',
            'base_model_dir_path': '',
            'base_model_meta_path': '',
            'base_model_sha256sum': '',
            'id': 1,
            'name': 'mock-base-model',
        }
        mocker.register_uri(
            'GET',
            config.url + '/base_models/1',
            status_code=200,
            json=mock_response,
        )
        response = bases.get_detail(1)
        self.assertIsInstance(response, dict)

    @requests_mock.Mocker()
    def test_bases_delete_all_images(self, mocker):
        mock_response = {
            'task_id': 'd4f79ce0-440b-4da2-ad8a-d7522d564246',
        }
        mocker.register_uri(
            'DELETE',
            config.url + '/base_models/1/delete_all_images/',
            status_code=200,
            json=mock_response,
        )
        response = bases.delete_all_images(1)
        self.assertIsInstance(response, dict)
        self.assertIn('task_id', response)
        self.assertTrue(self.is_valid_uuid4(response['task_id']))
