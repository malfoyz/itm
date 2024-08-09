import pytest

from ifelse.task3 import largest_and_smallest_numbers


@pytest.mark.parametrize('num1,num2,expected_result',
                         [(1, 5, {'min': 1, 'max': 5}),
                          (1000, -2000, {'min': -2000, 'max': 1000}),
                          (4, 4, {'min': 4, 'max': 4})])
def test_largest_and_smallest_numbers(num1, num2, expected_result):
    assert largest_and_smallest_numbers(num1, num2) == expected_result