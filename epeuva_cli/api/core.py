import json
import logging
import requests

from epeuva_cli.utils.config import config
from epeuva_cli.utils.output_handler import output


logger = logging.getLogger(__name__)


def create_login_token():
    output.debug('Creating login token')

    config.token = 'token_placeholder'

    credentials = {
        'username': config.username,
        'password': config.password,
    }

    token = post('/auth/login/', data=credentials).get('auth_token', None)

    config.token = token
    if not config.token:
        raise Exception('Failed to get login token.')

    config.headers = {
        'Authorization': 'token {}'.format(config.token),
    }
    output.debug('Token: {}'.format(config.token))


def do_request(
        callback,
        endpoint,
        params=None,
        data=None,
        files=None
    ):
    if not config.token:
        create_login_token()
    res = callback(
        config.url + endpoint,
        headers=config.headers,
        params=params,
        data=data,
        files=files,
    )
    try:
        res.raise_for_status()
        if res.content:
            return res.json()
        return {}
    except requests.exceptions.HTTPError as e:
        if isinstance(e.response.text, str):
            return e.response.text
        return json.loads(e.response.text)


def get(endpoint, params=None):
    return do_request(
        requests.get, endpoint, params=params
    )


def post(endpoint, params=None, data=None, files=None):
    return do_request(
        requests.post, endpoint, params=params, data=data, files=files
    )


def patch(endpoint, params=None, data=None):
    return do_request(
        requests.patch, endpoint, params=params, data=data
    )


def put(endpoint, params=None, data=None):
    return do_request(
        requests.put, endpoint, params=params, data=data
    )


def delete(endpoint, params=None):
    return do_requests(
        requests.delete, endpoint, params=params
    )
