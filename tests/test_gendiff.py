import pytest
from gendiff.gendiff import generate_diff
from tests.fixtures.expected_result import PLAIN_DIFF_1_2, PLAIN_DIFF_2_1
from tests.fixtures.expected_result import NESTED_STYLISH_DIFF_STR_12
from tests.fixtures.expected_result import PLAIN_NESTED_DIFF_1_2

@pytest.mark.parametrize("make_diff_args, expected",
                         [
                             (('./tests/fixtures/plain1.json', './tests/fixtures/plain2.json'),
                              PLAIN_DIFF_1_2),
                             (('./tests/fixtures/plain2.yaml', './tests/fixtures/plain1.yml'),
                              PLAIN_DIFF_2_1),
                             (('./tests/fixtures/nested1.json', './tests/fixtures/nested2.json'),
                              NESTED_STYLISH_DIFF_STR_12),
                             (('./tests/fixtures/nested1.yaml', './tests/fixtures/nested2.yaml'),
                              NESTED_STYLISH_DIFF_STR_12),
                             (('./tests/fixtures/nested1.json', './tests/fixtures/nested2.json', 'plain'),
                              PLAIN_NESTED_DIFF_1_2)
                         ]
                         )
def test_gendiff(make_diff_args, expected):
    assert generate_diff(*make_diff_args) == expected
