import pathlib
import json
import yaml


def get_extension(file_path):
    return pathlib.Path(file_path).suffix


def get_reader(file_path):
    return {
        '.json': json.load,
        '.yml': yaml.safe_load,
        '.yaml': yaml.safe_load
    }.get(get_extension(file_path))


def open_file(file_path):
    reader = get_reader(file_path)
    with open(file_path) as dictionary:
        return reader(dictionary)
