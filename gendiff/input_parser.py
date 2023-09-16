import json
import yaml


def parse(content, extension):
    reader = {
        '.json': json.load,
        '.yml': yaml.safe_load,
        '.yaml': yaml.safe_load
    }.get(extension)
    return reader(content)
