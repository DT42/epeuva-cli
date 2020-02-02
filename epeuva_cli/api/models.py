from epeuva_cli.api import core


def get_list(app_id):
    if app_id:
        params = {
            'base_model__app': app_id
        }
        return core.get('/models', params=params)
    return core.get('/models')


def get_detail(id):
    return core.get('/models/{}'.format(id))


def update_detail(id):
    return core.patch('/models/{}/'.format(id))


def delete_detail(id):
    return core.delete('/models/{}/'.format(id))


def test_images(id, files):
    return core.post(
        '/models/{}/test_images/'.format(id),
        files={'imgs': files},
    )


def test_videos(id, files):
    return core.post(
        '/models/{}/test_videos/'.format(id),
        files={'video': files},
    )
