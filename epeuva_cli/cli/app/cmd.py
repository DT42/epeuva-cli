import click

from epeuva_cli.cli.epeuva import cli
from epeuva_cli.api import apps
from epeuva_cli.utils.output_handler import output


@cli.group()
def app():
    pass


@app.command(name='list')
def get_list():
    result = apps.get_list()
    output.print(result)


@app.command()
@click.option('--id', prompt=True)
def detail(id):
    result = apps.get_detail(id)
    output.print(result)
