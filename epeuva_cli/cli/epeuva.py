import click
import logging
import pkg_resources

from epeuva_cli.api.core import create_login_token
from epeuva_cli.utils.output_handler import output


logger = logging.getLogger(__name__)


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    version = pkg_resources.require('epeuva-cli')[0].version
    output.print('Epeuva-CLI Version {}'.format(version))
    ctx.exit()


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.option('--pretty/--raw', default=True)
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def cli(debug, pretty):
    output.set(debug, pretty)
    create_login_token()


if __name__ == '__main__':
    cli()
