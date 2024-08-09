import pytest

from block2.task8 import reverse_number


@pytest.mark.parametrize('number,expected_result',
                         [(84, 48),
                          (32, 23)])
def test_reverse_number(number, expected_result):
    assert reverse_number(number) == expected_result


@pytest.mark.parametrize('number',
                         [0, 5, 100])
def test_reverse_number_value_error(number):
    with pytest.raises(ValueError):
        reverse_number(number)


