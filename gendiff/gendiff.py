from gendiff.input_parser import open_file
from gendiff.ast_maker import make_ast
from gendiff.formatters.stylish import gen_stylish_diff


def make_diff(first_file, second_file, format_type='stylish'):
    old = open_file(first_file)
    new = open_file(second_file)
    return {'stylish': gen_stylish_diff}[format_type](make_ast(old, new))
