import pytest

from task8 import calculate_squares_of_numbers


@pytest.mark.parametrize('min,max,expected_result',
                         [(2, 5, [4, 9, 16, 25]),
                          (-3, 3, [9, 4, 1, 0, 1, 4, 9])])
def test_calculate_squares_of_numbers_with_correct_data(min, max, expected_result):
    assert calculate_squares_of_numbers(min, max) == expected_result


def test_calculate_squares_of_numbers_with_uncorrect_data():
    with pytest.raises(Exception):
        calculate_squares_of_numbers(20, 10)