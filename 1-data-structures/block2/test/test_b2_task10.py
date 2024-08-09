import pytest

from block2.task10 import get_last_and_average_digit


@pytest.mark.parametrize('number,expected_result',
                         [(845, (5, 4)),
                          (124, (4, 2))])
def test_get_last_and_average_digit(number, expected_result):
    assert get_last_and_average_digit(number) == expected_result


@pytest.mark.parametrize('number',
                         [0, 53, 1000])
def test_get_last_and_average_digit_value_error(number):
    with pytest.raises(ValueError):
        get_last_and_average_digit(number)


