from epeuva_cli.api import core


def get_list():
    return core.get('/images')


def get_detail(id):
    return core.get('/images/{}'.format(id))


def update_detail(id):
    return core.patch('/images/{}/'.format(id))


def delete_detail(id):
    return core.delete('/images/{}/'.format(id))
