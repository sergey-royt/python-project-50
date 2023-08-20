import pytest
from gendiff.scripts.gendiff import generate_diff
from tests.fixtures.expected_result import PLAIN_1_2
from tests.fixtures.expected_result import PLAIN_2_1


@pytest.mark.parametrize("test_generate_diff, expected", [
    (('./tests/fixtures/plain1.json', './tests/fixtures/plain2.json'), PLAIN_1_2),
    (('./tests/fixtures/plain2.json', './tests/fixtures/plain1.json'), PLAIN_2_1)
]
                         )
def test_gendiff(test_generate_diff, expected):
    assert generate_diff(*test_generate_diff) == expected
