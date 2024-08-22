import pytest

from homework.dividers import get_dividers



@pytest.mark.parametrize('number, start, end, expected_result',
                         [(1000000, 1, 100, [1, 2, 4, 5, 8, 10, 16, 20, 25, 32, 40, 50, 64, 80, 100]),
                          (2000000, 300000, 2000001, [400000, 500000, 1000000, 2000000]),
                          (15000000, 4000000, 15000000, [5000000, 7500000, 15000000])])
def test_get_dividers(number, start, end, expected_result):
    assert get_dividers(number, start, end) == expected_result


@pytest.mark.parametrize('number, start, end',
                         [('string', 1, 2000),
                          (2000.72, 4000, 20000),
                          (350000, 'new_string', 20.7),
                          (400000, 400.5, 'old_string')])
def test_get_dividers_with_type_error(number, start, end):
    with pytest.raises(TypeError):
        get_dividers(number, start, end)


@pytest.mark.parametrize('number, start, end',
                         [(1, 1, 1),
                          (999999, 1, 999999),
                          (20000001, 1, 2500000),
                          (3000000, 3000000, 1000000)])
def test_get_dividers_with_value_error(number, start, end):
    with pytest.raises(ValueError):
        get_dividers(number, start, end)