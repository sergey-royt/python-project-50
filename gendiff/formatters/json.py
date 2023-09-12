import json


def gen_json_diff(diff_dict):
    return json.dumps(diff_dict, indent=1)
