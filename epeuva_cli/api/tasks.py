from epeuva_cli.api import core


def get_list():
    return core.get('/tasks')


def get_detail(uuid):
    return core.get('/tasks/{}'.format(uuid))
