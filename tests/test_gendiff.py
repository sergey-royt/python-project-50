import pytest
from gendiff.gendiff import generate_diff
from tests.fixtures.expected_result import PLAIN_JSON_1_2, PLAIN_JSON_2_1
from tests.fixtures.expected_result import PLAIN_YAML_1_2, PLAIN_YAML_2_1


@pytest.mark.parametrize("test_generate_diff, expected", [
    (('./tests/fixtures/plain1.json',
      './tests/fixtures/plain2.json'), PLAIN_JSON_1_2),
    (('./tests/fixtures/plain2.json',
      './tests/fixtures/plain1.json'), PLAIN_JSON_2_1),
    (('./tests/fixtures/plain1.yml',
      './tests/fixtures/plain2.yml'), PLAIN_YAML_1_2),
    (('./tests/fixtures/plain1.yaml',
      './tests/fixtures/plain2.yaml'), PLAIN_YAML_1_2),
    (('./tests/fixtures/plain2.yml',
      './tests/fixtures/plain1.yml'), PLAIN_YAML_2_1),
    (('./tests/fixtures/plain2.yaml',
      './tests/fixtures/plain1.yaml'), PLAIN_YAML_2_1)
]
                         )
def test_gendiff(test_generate_diff, expected):
    assert generate_diff(*test_generate_diff) == expected
