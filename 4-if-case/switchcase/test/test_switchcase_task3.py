import pytest

from switchcase.task3 import next_date


@pytest.mark.parametrize('month,day,expected_result',
                         [(12, 1, (12, 2)),
                          (10, 4, (10, 5))])
def test_next_date_correct(month, day, expected_result):
    assert next_date(month, day) == expected_result


@pytest.mark.parametrize('month,day',
                         [(-1, 13),
                          (13, 15),
                          (5, 0),
                          (7, 32)])
def test_next_date_uncorrect(month, day):
    with pytest.raises(Exception):
        next_date(month_number)
