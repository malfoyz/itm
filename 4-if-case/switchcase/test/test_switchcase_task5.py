import pytest

from switchcase.task5 import number_description


@pytest.mark.parametrize('number,expected_result',
                         [(123, 'сто двадцать три'),
                          (990, 'девятьсот девяносто ')])
def test_correct_number_description(number, expected_result):
    assert number_description(number) == expected_result


def test_uncorrect_number_description():
    with pytest.raises(Exception):
        number_description(1023)
