def _stringify_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, int):
        return str(value)
    special_values = {
        'True': 'true',
        'False': 'false',
        'None': 'null',
        '': "''"
    }
    str_value = str(value)
    return special_values.get(str_value, f"'{str_value}'")


def _stringify(status, content, path):
    if status == 'changed':
        old_content, new_content = content
        return f"\
Property '{'.'.join(path)}' was updated.\
 From {_stringify_value(old_content)} to {_stringify_value(new_content)}"
    elif status == 'added':
        return f"\
Property '{'.'.join(path)}' was added with value: {_stringify_value(content)}"
    else:
        return f"Property '{'.'.join(path)}' was removed"


def gen_plain_diff(dict_diff):
    tokens = []

    def helper(current_dict, path):
        for key in sorted(current_dict):
            current_path = path + (key,)
            value = current_dict[key]
            if isinstance(value, dict):
                helper(value, current_path)
                continue

            status, content = value
            if status == 'unchanged':
                continue
            else:
                tokens.append(_stringify(status, content, current_path))
        return '\n'.join(tokens)
    return helper(dict_diff, tuple())
