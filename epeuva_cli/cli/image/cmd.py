import click

from epeuva_cli.cli.epeuva import cli
from epeuva_cli.api import images
from epeuva_cli.utils.output_handler import output


@cli.group()
def image():
    pass


@image.command(name='list')
def get_list():
    result = images.get_list()
    output.print(result)


@image.group()
@click.option('--id', prompt=True)
@click.pass_context
def detail(ctx, id):
    ctx.ensure_object(dict)
    ctx.obj['id'] = id


@detail.command()
@click.pass_context
def show(ctx):
    result = images.get_detail(ctx.obj['id'])
    output.print(result)


@detail.command()
@click.pass_context
def update(ctx):
    result = images.update_detail(ctx.obj['id'])
    output.print(result)


@detail.command()
@click.pass_context
def delete(ctx):
    result = images.delete_detail(ctx.obj['id'])
    output.print(result)
