import pathlib
from gendiff.input_parser import parse
from gendiff.ast_maker import make_ast
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import gen_json_diff


def get_file_data(file):
    extension = pathlib.Path(file).suffix
    content = open(file, 'r')
    return parse(content, extension)


def generate_diff(first_file, second_file, format_type='stylish'):
    old = get_file_data(first_file)
    new = get_file_data(second_file)
    return {'stylish': stylish,
            'plain': plain,
            'json': gen_json_diff}[format_type](make_ast(old, new))
