from epeuva_cli.api import core


def get_list(app_id, base_id):
    params = {}
    if app_id:
        params['app'] = app_id
    if base_id:
        params['base_model'] = base_id
    return core.get('/labels', params=params)


def get_detail(id):
    return core.get('/labels/{}'.format(id))


def list_images(id):
    return core.get('/labels/{}/list_images'.format(id))


def upload_image(id, files):
    return core.post(
        '/labels/{}/upload_image/'.format(id),
        files={'img': files}
    )


def delete_all_images(id):
    return core.delete('/labels/{}/delete_all/'.format(id))
