import json
import yaml


def parse(data_path, extension):
    reader = {
        '.json': json.load,
        '.yml': yaml.safe_load,
        '.yaml': yaml.safe_load
    }.get(extension)
    with open(data_path, 'r') as file_data:
        return reader(file_data)
