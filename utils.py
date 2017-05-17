__author__ = 'tom caruso'

import pathlib


def ensure_path_exists(filepath):
    p = pathlib.Path(filepath)
    if not p.exists():
        p.mkdir()
