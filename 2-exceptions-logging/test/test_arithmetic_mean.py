import pytest

from logging_tasks.homework.arithmetic_mean import arithmetic_mean


@pytest.mark.parametrize('numbers,expected_result',
                         [([2, 4, 6, 10], 5.5),
                          ([-2.2, 2.2, -2.2, 2.2], 0),
                          ([0, 0, 0, 0, 0, 0], 0)])
def test_arithmetic_mean_with_correct_data(numbers, expected_result):
    assert arithmetic_mean(numbers) == expected_result


@pytest.mark.parametrize('numbers',
                         [[],
                          ['sas', 1, -2],
                          1,
                          'asfds'])
def test_arithmetic_mean_with_uncorrect_data(numbers):
    with pytest.raises(Exception):
        arithmetic_mean(numbers)
