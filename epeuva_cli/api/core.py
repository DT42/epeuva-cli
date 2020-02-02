import json
import logging
import requests

from epeuva_cli.utils.config import config
from epeuva_cli.utils.output_handler import output


logger = logging.getLogger(__name__)


def create_login_token():
    output.debug('Creating login token')
    if config.token:
        output.debug('Already has login token, skipping')
        return

    credentials = {
        'username': config.username,
        'password': config.password,
    }

    token = post(
                '/auth/login/',
                data=credentials,
            ).get('auth_token', None)
    if not token:
        raise Exception('Failed to get login token.')
    config.token = token
    config.headers = {
        'Authorization': 'token {}'.format(config.token),
    }
    output.debug('Token: {}'.format(config.token))


def get(endpoint, params=None):
    res = requests.get(
        config.url + endpoint,
        params=params,
        headers=config.headers,
    )
    try:
        res.raise_for_status()
        if res.content:
            return res.json()
        return {}
    except requests.exceptions.HTTPError as e:
        return json.loads(e.response.text)


def post(endpoint, params=None, data=None, files=None):
    res = requests.post(
        config.url + endpoint,
        params=params,
        data=data,
        files=files,
        headers=config.headers,
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


def patch(endpoint, params=None, data=None):
    res = requests.patch(
        config.url + endpoint,
        params=params,
        data=data,
        headers=config.headers,
    )
    try:
        res.raise_for_status()
        if res.content:
            return res.json()
        return {}
    except requests.exceptions.HTTPError as e:
        return json.loads(e.response.text)


def put(endpoint, params=None, data=None):
    res = requests.put(
        config.url + endpoint,
        params=params,
        data=data,
        headers=config.headers,
    )
    try:
        res.raise_for_status()
        if res.content:
            return res.json()
        return {}
    except requests.exceptions.HTTPError as e:
        return json.loads(e.response.text)


def delete(endpoint, params=None):
    res = requests.delete(
        config.url + endpoint,
        params=params,
        headers=config.headers,
    )
    try:
        res.raise_for_status()
        if res.content:
            return res.json()
        return {}
    except requests.exceptions.HTTPError as e:
        return json.loads(e.response.text)


create_login_token()
