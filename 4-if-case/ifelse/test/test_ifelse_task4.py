import pytest

from ifelse.task4 import find_smallest_number


@pytest.mark.parametrize('num1,num2,num3,expected_result',
                         [(1, 5, 10, 1),
                          (-3.2, 5, -10.1, -10.1),
                          (0, 0, 0, 0)])
def test_find_smallest_number(num1, num2, num3, expected_result):
    assert find_smallest_number(num1, num2, num3) == expected_result