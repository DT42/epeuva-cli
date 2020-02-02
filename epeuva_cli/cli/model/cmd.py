import click

from epeuva_cli.cli.epeuva import cli
from epeuva_cli.api import models
from epeuva_cli.utils.config import config
from epeuva_cli.utils.download import chunk_download
from epeuva_cli.utils.output_handler import output


@cli.group()
def model():
    pass


@model.command(name='list')
@click.option('--app-id')
def get_list(app_id):
    result = models.get_list(app_id)
    output.print(result)


@model.group()
@click.option('--id', prompt=True)
@click.pass_context
def detail(ctx, id):
    ctx.ensure_object(dict)
    ctx.obj['id'] = id


@detail.command()
@click.pass_context
def show(ctx):
    result = models.get_detail(ctx.obj['id'])
    output.print(result)


@detail.command()
@click.pass_context
def update(ctx):
    result = models.update_detail(ctx.obj['id'])
    output.print(result)


@detail.command()
@click.pass_context
def delete(ctx):
    result = models.delete_detail(ctx.obj['id'])
    output.print(result)


@detail.command()
@click.pass_context
def test_images(ctx):
    result = models.test_images(ctx.obj['id'])
    output.print(result)


@detail.command()
@click.pass_context
def test_videos(ctx):
    result = models.test_videos(ctx.obj['id'])
    output.print(result)


@detail.command()
@click.option('--converted', is_flag=True)
@click.pass_context
def download(ctx, converted):
    result = models.get_detail(ctx.obj['id'])
    if converted:
        model_path_key = 'converted_zip_url'
    else:
        model_path_key = 'zip_url'
    model_path = result[model_path_key]

    host_url = config.url.replace('/api/v1', '')
    model_url = '{}/{}'.format(host_url, model_path)
    filename = model_url.split('/')[-1]

    chunk_download(model_url, filename)
    output.print({'download_status': 'SUCCESS'})
