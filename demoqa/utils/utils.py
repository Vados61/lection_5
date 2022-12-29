import os


def media_path(file_name):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, '../media', file_name))
