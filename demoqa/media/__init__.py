import os.path

media_path = os.path.dirname(__file__)


def path(file_name):
    return os.path.abspath(os.path.join(media_path, file_name))
