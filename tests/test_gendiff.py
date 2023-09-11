import pytest
from gendiff.gendiff import make_diff
from tests.fixtures.expected_result import PLAIN_JSON_1_2, PLAIN_JSON_2_1
from tests.fixtures.expected_result import PLAIN_YAML_1_2, PLAIN_YAML_2_1
from tests.fixtures.expected_result import NESTED_STYLISH_DIFF_STR_12


@pytest.mark.parametrize("test_generate_diff, expected", [
    (('./tests/fixtures/plain1.json',
      './tests/fixtures/plain2.json', 'stylish'), PLAIN_JSON_1_2),
    (('./tests/fixtures/plain2.json',
      './tests/fixtures/plain1.json', 'stylish'), PLAIN_JSON_2_1),
    (('./tests/fixtures/plain1.yml',
      './tests/fixtures/plain2.yml', 'stylish'), PLAIN_YAML_1_2),
    (('./tests/fixtures/plain1.yaml',
      './tests/fixtures/plain2.yaml', 'stylish'), PLAIN_YAML_1_2),
    (('./tests/fixtures/plain2.yml',
      './tests/fixtures/plain1.yml', 'stylish'), PLAIN_YAML_2_1),
    (('./tests/fixtures/plain2.yaml',
      './tests/fixtures/plain1.yaml', 'stylish'), PLAIN_YAML_2_1),
    (('./tests/fixtures/nested1.json',
      './tests/fixtures/nested2.json', 'stylish'), NESTED_STYLISH_DIFF_STR_12),
    (('./tests/fixtures/nested1.yaml',
      './tests/fixtures/nested2.yaml', 'stylish'), NESTED_STYLISH_DIFF_STR_12)
]
                         )
def test_gendiff(test_generate_diff, expected):
    assert make_diff(*test_generate_diff) == expected
