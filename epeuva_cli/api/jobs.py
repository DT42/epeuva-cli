from epeuva_cli.api import core


def get_list(app_id):
    if app_id:
        params = {
            'app': app_id
        }
        return core.get('/jobs', params=params)
    return core.get('/jobs')


def get_detail(id):
    return core.get('/jobs/{}'.format(id))


def delete_detail(id):
    return core.delete('/jobs/{}/'.format(id))


def retrain(app_id, model_name, labels, note):
    payload = {
        'app': app_id,
        'model_name': model_name,
        'labels': labels,
        'note': note,
    }
    return core.post('/jobs/retrain/'.format(id), data=payload)


def convert(app_id, model_name, model_id, platform):
    payload = {
        'app': app_id,
        'model_name': model_name,
        'model_id': model_id,
        'platform': platform,
    }
    return core.post('/jobs/convert/'.format(id), data=payload)
