def make_ast(old_dict, new_dict):
    diff_dict = []

    for key in sorted(list({**old_dict, **new_dict}.keys())):
        if key not in old_dict:
            diff_dict.append({
                'key': key,
                'action': 'added',
                'value': new_dict[key]
            })

        elif key not in new_dict:
            diff_dict.append({
                'key': key,
                'action': 'deleted',
                'value': old_dict[key]
            })

        elif isinstance(
                old_dict[key], dict) and isinstance(new_dict[key], dict):
            diff_dict.append({
                'key': key,
                'action': 'nested',
                'children': make_ast(old_dict[key], new_dict[key])
            })
        elif old_dict[key] == new_dict[key]:
            diff_dict.append({
                'key': key,
                'action': 'unchanged',
                'value': old_dict[key],
            })

        else:
            diff_dict.append({
                'key': key,
                'action': 'changed',
                'old_value': old_dict[key],
                'new_value': new_dict[key]
            })

    return diff_dict
