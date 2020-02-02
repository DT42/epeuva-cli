import click

from epeuva_cli.cli.epeuva import cli
from epeuva_cli.api import tasks
from epeuva_cli.utils.output_handler import output


@cli.group()
def task():
    pass


@task.command(name='list')
def get_list():
    result = tasks.get_list()
    output.print(result)


@task.group()
@click.option('--uuid', '-u', prompt=True)
@click.pass_context
def detail(ctx, uuid):
    ctx.ensure_object(dict)
    ctx.obj['uuid'] = uuid


@detail.command()
@click.pass_context
def show(ctx):
    result = tasks.get_detail(ctx.obj['uuid'])
    output.print(result)
