from epeuva_cli.api import core


def get_list(app_id):
    if app_id:
        params = {
            'app': app_id
        }
        return core.get('/base_models', params=params)
    return core.get('/base_models')


def get_detail(id):
    return core.get('/base_models/{}'.format(id))


def delete_all_images(id):
    return core.delete('/base_models/{}/delete_all_images/'.format(id))
