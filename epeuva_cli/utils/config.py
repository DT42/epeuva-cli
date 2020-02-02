import click
import configparser
import logging
import os
import sys


logger = logging.getLogger(__name__)


DEFAULT_CONFIG = os.path.expanduser('~/.epeuva-cli.conf')


class Config():
    def __init__(self):
        logger.debug('Initiating config')
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

        if not 'host' in config:
            raise ConfigError('[host] section not defined in config.')
        if not 'url' in config['host']:
            raise ConfigError('url not defined in [host] section of the config.')

        if not 'user' in config:
            raise ConfigError('[user] section not defined in config.')
        if not 'username' in config['user']:
            raise ConfigError('username not defined in [user] section of the config.')
        if not 'password' in config['user']:
            raise ConfigError('password not defined in [user] section of the config.')

        return config

    def new(self):
        click.echo('')
        if not click.confirm('Would like to generate/update the config?'):
            click.echo('Aborting')
            sys.exit()

        url = click.prompt('Please enter the host url', type=str)
        username = click.prompt('Please enter the username', type=str)
        password = click.prompt('Please enter the password', type=str, hide_input=True)

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
