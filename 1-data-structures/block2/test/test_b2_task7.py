import pytest

from block2.task7 import calculate_digits_sum_comp


@pytest.mark.parametrize('number,expected_result',
                         [(84, (12, 32)),
                          (32, (5, 6))])
def test_calculate_digits_sum_comp(number, expected_result):
    assert calculate_digits_sum_comp(number) == expected_result


@pytest.mark.parametrize('number',
                         [0, 5, 100])
def test_calculate_digits_sum_comp_value_error(number):
    with pytest.raises(ValueError):
        calculate_digits_sum_comp(number)


