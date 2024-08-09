import pytest

from task7 import find_prime_numbers


@pytest.mark.parametrize('min,max,expected_result',
                         [(2, 20, [2, 3, 5, 7, 11, 13, 17, 19]),
                          (30, 50, [31, 37, 41, 43, 47])])
def test_find_prime_number_with_correct_data(min, max, expected_result):
    assert find_prime_numbers(min, max) == expected_result


@pytest.mark.parametrize('min,max',
                         [(1, 20),
                          (10, 1)])
def test_find_prime_number_with_uncorrect_data(min, max):
    with pytest.raises(Exception):
        find_prime_numbers(min, max)