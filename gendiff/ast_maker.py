def set_value(dictionary, path, value):
    if len(path) != 0:
        current = dictionary
        for key in path[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]
        current[path[-1]] = value


def helper(dict_old, dict_new, path, diff_dict):

    old_keys = dict_old.keys()
    new_keys = dict_new.keys()

    added_keys = new_keys - old_keys
    deleted_keys = old_keys - new_keys
    common_keys = new_keys & old_keys

    for key in added_keys:
        set_value(diff_dict, path + (key,),
                  ('added', dict_new[key]))

    for key in deleted_keys:
        set_value(diff_dict, path + (key,),
                  ('deleted', dict_old[key]))

    for key in common_keys:
        value_new = dict_new[key]
        value_old = dict_old[key]

        if isinstance(value_new, dict) and isinstance(value_old, dict):
            helper(value_old, value_new, path + (key,), diff_dict)
        elif value_new != value_old:
            set_value(diff_dict, path + (key,),
                      ('changed', (value_old, value_new)))
        else:
            set_value(diff_dict, path + (key,),
                      ('unchanged', value_old))


def make_ast(old_dict, new_dict):
    diff_dict = {}
    helper(old_dict, new_dict, tuple(), diff_dict)
    return diff_dict
