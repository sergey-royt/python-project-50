import pathlib
from gendiff.input_parser import parse
from gendiff.ast_maker import make_ast
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import gen_json_diff


def generate_diff(first_file, second_file, format_type='stylish'):
    old = parse(first_file, pathlib.Path(first_file).suffix)
    new = parse(second_file, pathlib.Path(second_file).suffix)
    return {'stylish': stylish,
            'plain': plain,
            'json': gen_json_diff}[format_type](make_ast(old, new))
