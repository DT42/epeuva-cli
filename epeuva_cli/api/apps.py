from epeuva_cli.api import core


def get_list():
    return core.get('/apps')


def get_detail(id=1):
    return core.get('/apps/{}'.format(id))
