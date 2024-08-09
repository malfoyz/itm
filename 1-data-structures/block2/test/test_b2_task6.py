import pytest

from block2.task6 import calculate_digits


def test_calculate_digits():
    assert calculate_digits(84) == (8, 4)


@pytest.mark.parametrize('number',
                         [0, 5, 100])
def test_calculate_digits_value_error(number):
    with pytest.raises(ValueError):
        calculate_digits(number)


