import requests
import os

from tqdm import tqdm


def chunk_download(url, filename):
    try:
        dl = requests.get(url, stream=True)
        total_size = int(dl.headers.get('content-length', 0))
        t=tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(filename, 'wb') as f:
            for chunk in dl.iter_content(chunk_size=1024):
                if chunk:
                    t.update(len(chunk))
                    f.write(chunk)
        t.close()
    except (requests.exceptions.HTTPError, OSError):
        raise
