import pytest

from task10 import factorials


def test_factorials_with_default_parameters():
    assert factorials() == [1, 2, 6, 24, 120]

@pytest.mark.parametrize('start,stop,expected_result',
                         [(5, 8, [120, 720, 5040, 40320]),
                          (10, 12, [3628800, 39916800, 479001600])])
def test_factorials_with_correct_data(start, stop, expected_result):
    assert factorials(start, stop) == expected_result


@pytest.mark.parametrize('start,stop',
                         [(0, 10),
                          (10, 3)])
def test_factorials_with_uncorrect_data(start, stop):
    with pytest.raises(Exception):
        factorials(start, stop)