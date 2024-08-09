import pytest

from task9 import calculate_squares_of_numbers


@pytest.mark.parametrize('min,max,step,expected_result',
                         [(2, 10, 2, [4, 16, 36, 64, 100]),
                          (-6, 6, 3, [36, 9, 0, 9, 36])])
def test_calculate_squares_of_numbers_with_correct_data(min, max, step, expected_result):
    assert calculate_squares_of_numbers(min, max, step) == expected_result


def test_calculate_squares_of_numbers_with_uncorrect_data():
    with pytest.raises(Exception):
        calculate_squares_of_numbers(20, 10, 2)