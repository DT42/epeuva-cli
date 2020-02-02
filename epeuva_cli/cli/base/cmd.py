import click

from epeuva_cli.cli.epeuva import cli
from epeuva_cli.api import bases
from epeuva_cli.utils.output_handler import output


@cli.group()
def base():
    pass


@base.command(name='list')
@click.option('--app-id')
def get_list(app_id):
    result = bases.get_list(app_id)
    output.print(result)


@base.group()
@click.option('--id', prompt=True)
@click.pass_context
def detail(ctx, id):
    ctx.ensure_object(dict)
    ctx.obj['id'] = id


@detail.command()
@click.pass_context
def show(ctx):
    result = bases.get_detail(ctx.obj['id'])
    output.print(result)


@detail.command()
@click.option('--yes', '-y', is_flag=True)
@click.pass_context
def delete_all_images(ctx, yes):
    if not yes:
        click.confirm(
            'Are you sure you want to delete all images for this base model?',
            abort=True
        )
    result = bases.delete_all_images(ctx.obj['id'])
    output.print(result)
