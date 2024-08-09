import pytest

from block1.task10 import calculate_arithmetic_operations


@pytest.mark.parametrize('a,b,expected_result',
                         [(4, 4, (8, 0, 16, 1)),
                          (5.5, 6.5, (12, -1, 35.75, 0.8461538461538461)),
                          (-4, -4, (-8, 0, 16, 1))])
def test_calculate_arithmetic_operations(a, b, expected_result):
    assert calculate_arithmetic_operations(a, b) == expected_result


def test_calculate_arithmetic_operations_with_zero():
    with pytest.raises(ZeroDivisionError):
        calculate_arithmetic_operations(4, 0)