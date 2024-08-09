import pytest

from block2.task9 import get_first_digit


@pytest.mark.parametrize('number,expected_result',
                         [(843, 8),
                          (324, 3)])
def test_get_first_digit(number, expected_result):
    assert get_first_digit(number) == expected_result


@pytest.mark.parametrize('number',
                         [0, 53, 1000])
def test_reverse_number_value_error(number):
    with pytest.raises(ValueError):
        get_first_digit(number)


