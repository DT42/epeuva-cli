import click
import configparser
import logging
import os
import sys


logger = logging.getLogger(__name__)


DEFAULT_CONFIG = os.path.expanduser('~/.epeuva-cli.conf')
EPEUVA_USE_CI = os.environ['EPEUVA_USE_CI']


class Config():

    def __init__(self):
        logger.debug('Initiating config')
        if EPEUVA_USE_CI:
            conf = self.load_dummy_config()
        else:
            try:
                conf = self.load()
            except (ConfigError, OSError) as e:
                logger.debug('Failed to load config')
                click.echo(e)
                self.new()
        logger.debug('Successfully loaded config')
        self.url = conf['host']['url']
        self.username = conf['user']['username']
        self.password = conf['user']['password']
        self.token = None
        self.headers = {}

    def load(self):
        if not os.path.exists(DEFAULT_CONFIG):
            raise FileNotFoundError(2, 'Config file not found', DEFAULT_CONFIG)

        config = configparser.ConfigParser()
        try:
            config.read(DEFAULT_CONFIG)
        except configparser.Error:
            raise

        if 'host' not in config:
            raise ConfigError('[host] section not defined in config.')
        if 'url' not in config['host']:
            raise ConfigError(
                'url not defined in [host] section of the config.'
            )

        if 'user' not in config:
            raise ConfigError('[user] section not defined in config.')
        if 'username' not in config['user']:
            raise ConfigError(
                'username not defined in [user] section of the config.'
            )
        if 'password' not in config['user']:
            raise ConfigError(
                'password not defined in [user] section of the config.'
            )

        return config

    def load_dummy_config(self):
        config = configparser.ConfigParser()
        config['host'] = {
            'url': 'https://epeuva-cli.ci/api/v1'
        }
        config['user'] = {
            'username': 'ci',
            'password': 'ci',
        }

        return config

    def new(self):
        click.echo('')
        if not click.confirm('Would like to generate/update the config?'):
            click.echo('Aborting')
            sys.exit()

        url = click.prompt('Please enter the host url', type=str)
        username = click.prompt('Please enter the username', type=str)
        password = click.prompt(
            'Please enter the password', type=str, hide_input=True
        )

        config = configparser.ConfigParser()
        config['host'] = {
            'url': url,
        }
        config['user'] = {
            'username': username,
            'password': password,
        }

        try:
            with open(DEFAULT_CONFIG, 'w') as configfile:
                config.write(configfile)
        except OSError:
            raise

        click.echo('')
        click.echo('Config file created. Please run the CLI command again.')
        sys.exit()


class ConfigError(Exception):
    pass


config = Config()
