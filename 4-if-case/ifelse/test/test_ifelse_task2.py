import pytest

from ifelse.task2 import largest_number


@pytest.mark.parametrize('num1,num2,expected_result',
                         [(1, 5, 5),
                          (1000, -2000, 1000),
                          (4, 4, 4)])
def test_largest_number(num1, num2, expected_result):
    assert largest_number(num1, num2) == expected_result