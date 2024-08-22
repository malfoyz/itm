import pytest

from homework.dividers import get_dividers, get_dividers_with_mulptiprocessing


@pytest.mark.parametrize('number',
                         [1000000, 2000000, 15000000])
def test_get_dividers_with_multiprocessing(number):
    expected_result = get_dividers(number, 1, number)
    result = get_dividers_with_mulptiprocessing(number)
    assert result == expected_result


@pytest.mark.parametrize('number',
                         ['string', 2000.72])
def test_get_dividers_with_multiprocessing_type_error(number):
    with pytest.raises(TypeError):
        get_dividers_with_mulptiprocessing(number)


@pytest.mark.parametrize('number',
                         [1, 999999, 20000001])
def test_get_dividers_with_multiprocessing_value_error(number):
    with pytest.raises(ValueError):
        get_dividers_with_mulptiprocessing(number)
