import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', action='store')
    parser.add_argument('second_file', action='store')
    parser.add_argument('-f', '--format', metavar='FORMAT', action='store',
                        help='set format of output')
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file))


def diff_to_str(diff):
    result = '{\n'
    for k, v in sorted(diff.items()):
        if v[0] == 'added':
            result += f'  + {k} : {v[-1]}\n'
        elif v[0] == 'deleted':
            result += f'  - {k} : {v[1]}\n'
        elif v[0] == 'unchanged':
            result += f'    {k} : {v[1]}\n'
        else:
            result += f'  - {k} : {v[1]}\n'
            result += f'  + {k} : {v[2]}\n'
    result += '}'
    return result


def generate_diff(first_file, second_file):
    with (
        open(first_file) as old_file,
        open(second_file) as new_file
    ):
        diff_dict = {}
        old_dictionary = json.load(old_file)
        new_dictionary = json.load(new_file)
        old_keys = old_dictionary.keys()
        new_keys = new_dictionary.keys()
        added_keys = new_keys - old_keys
        deleted_keys = old_keys - new_keys
        common_keys = new_keys & old_keys
        for key in added_keys:
            diff_dict[key] = ('added', new_dictionary[key])
        for key in deleted_keys:
            diff_dict[key] = ('deleted', old_dictionary[key])
        for key in common_keys:
            if old_dictionary[key] == new_dictionary[key]:
                diff_dict[key] = ('unchanged', old_dictionary[key])
            else:
                diff_dict[key] = (
                    'changed', old_dictionary[key], new_dictionary[key]
                )
        return diff_to_str(diff_dict)


if __name__ == '__main__':
    main()
