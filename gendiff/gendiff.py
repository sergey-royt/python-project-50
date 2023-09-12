from gendiff.input_parser import open_file
from gendiff.ast_maker import make_ast
from gendiff.formatters.stylish import gen_stylish_diff
from gendiff.formatters.plain import gen_plain_diff
from gendiff.formatters.json import gen_json_diff


def generate_diff(first_file, second_file, format_type='stylish'):
    old = open_file(first_file)
    new = open_file(second_file)
    return {'stylish': gen_stylish_diff,
            'plain': gen_plain_diff,
            'json': gen_json_diff}[format_type](make_ast(old, new))
