from tqdm import tqdm


def iterate(iterable, callback, arg,  unit='it'):
    """Iterate through the iterable with a progress bar

    Args:
    iterable: an iterable to be iterated
    callback (function): a callback to be called in each iteration
    unit: the unit showing in the progress bar
    """
    for i in tqdm(iterable, unit=unit):
        callback(i, arg)


def manual(total, callback, unit='it'):
    """Create a progress bar with manual updates

    Args:
    total (int): total progress steps
    callback (function): a callback to be called in each iteration
        must accept exactly one arg, the update progress callback,
        which accept steps as arg
        example: update(1) updates 1 step in progress
    unit: the unit showing in the progress bar
    """

    with tqdm(total=total, unit=unit) as pbar:
        callback(pbar.update)
