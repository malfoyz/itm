import pytest

from switchcase.task2 import days_in_month_count


@pytest.mark.parametrize('month_number,expected_result',
                         [(3, 31),
                          (9, 30),
                          (2, 28)])
def test_days_in_correct_month_count(month_number, expected_result):
    assert days_in_month_count(month_number) == expected_result


@pytest.mark.parametrize('month_number',
                         [13, 0, -2])
def test_days_in_uncorrect_month_count(month_number):
    with pytest.raises(Exception):
        days_in_month_count(month_number)
