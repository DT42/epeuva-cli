import click

from epeuva_cli.cli.epeuva import cli
from epeuva_cli.api import labels
from epeuva_cli.utils.output_handler import output


@cli.group()
def label():
    pass


@label.command(name='list')
@click.option('--app-id')
@click.option('--base-id')
def get_list(app_id, base_id):
    result = labels.get_list(app_id, base_id)
    output.print(result)


@label.group()
@click.option('--id', prompt=True)
@click.pass_context
def detail(ctx, id):
    ctx.ensure_object(dict)
    ctx.obj['id'] = id


@detail.command()
@click.pass_context
def show(ctx):
    result = labels.get_detail(ctx.obj['id'])
    output.print(result)


@detail.command()
@click.pass_context
def list_images(ctx):
    result = labels.list_images(ctx.obj['id'])
    output.print(result)


@detail.command()
@click.argument('files', type=click.File(mode='rb'), nargs=-1)
@click.pass_context
def upload_images(ctx, files):
    if len(files) < 2:
        files = [files]
    for file in files:
        result = labels.upload_image(ctx.obj['id'], file)
        output.print(result)
        # TODO: Progress Bar


@detail.command()
@click.option('--yes', '-y', is_flag=True)
@click.pass_context
def delete_all_images(ctx, yes):
    if not yes:
        click.confirm(
            'Are you sure you want to delete all images for this label?',
            abort=True
        )
    result = labels.delete_all_images(ctx.obj['id'])
    output.print(result)
