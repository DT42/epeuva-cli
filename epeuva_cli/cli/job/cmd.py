import click

from epeuva_cli.cli.epeuva import cli
from epeuva_cli.api import jobs
from epeuva_cli.utils.output_handler import output


@cli.group()
def job():
    pass


@job.command(name='list')
@click.option('--app-id')
def get_list(app_id):
    result = jobs.get_list(app_id)
    output.print(result)


@job.group()
@click.option('--id', prompt=True)
@click.pass_context
def detail(ctx, id):
    ctx.ensure_object(dict)
    ctx.obj['id'] = id


@detail.command()
@click.pass_context
def show(ctx):
    result = jobs.get_detail(ctx.obj['id'])
    output.print(result)


@detail.command()
@click.pass_context
def delete(ctx):
    result = jobs.delete_detail(ctx.obj['id'])
    output.print(result)


@job.command()
@click.option('--app-id', prompt=True)
@click.option('--model-name', prompt=True)
@click.option('--label-list', type=click.File(), prompt=True)
@click.option('--note')
def retrain(app_id, model_name, label_list, note):
    labels = label_list.read().splitlines()
    result = jobs.retrain(app_id, model_name, labels, note)
    output.print(result)


@job.command()
@click.option('--app-id', prompt=True)
@click.option('--model-name', prompt=True)
@click.option('--model-id', prompt=True)
@click.option('--platform', prompt=True)
def convert(app_id, model_name, model_id, platform):
    result = jobs.convert(app_id, model_name, model_id, platform)
    output.print(result)
