import pytest
from gendiff.gendiff import generate_diff

@pytest.mark.parametrize("make_diff_args, expected",
                         [
                             (('./tests/fixtures/plain1.json', './tests/fixtures/plain2.json'),
                              './tests/fixtures/stylish_plain_expected_12'),
                             (('./tests/fixtures/plain2.yaml', './tests/fixtures/plain1.yml'),
                              './tests/fixtures/stylish_plain_expected_21'),
                             (('./tests/fixtures/nested1.json', './tests/fixtures/nested2.json'),
                              './tests/fixtures/stylish_nested_expected_12'),
                             (('./tests/fixtures/nested1.yaml', './tests/fixtures/nested2.yaml'),
                              './tests/fixtures/stylish_nested_expected_12'),
                             (('./tests/fixtures/nested1.json', './tests/fixtures/nested2.json', 'plain'),
                              './tests/fixtures/plain_nested_expected_12'),
                             (('./tests/fixtures/nested1.yaml', './tests/fixtures/nested2.yaml', 'plain'),
                              './tests/fixtures/plain_nested_expected_12')
                         ]
                         )
def test_gendiff(make_diff_args, expected):
    expected = open(expected, 'r').read()
    assert generate_diff(*make_diff_args) == expected
