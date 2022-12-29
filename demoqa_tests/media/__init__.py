import os

path_dir = os.path.dirname(__file__)


def path_to_file(file_name):
    return os.path.join(path_dir, file_name)
