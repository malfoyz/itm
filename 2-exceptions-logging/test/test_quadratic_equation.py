import pytest

from logging_tasks.homework.quadratic_equation import quadratic_equation


@pytest.mark.parametrize('a,b,c,expected_result',
                         [(2, 2, 0, (0, -1)),
                          (-2, 0, 2, (-1, 1))])
def test_arithmetic_mean_with_correct_data(a, b, c, expected_result):
    assert quadratic_equation(a, b, c) == expected_result


@pytest.mark.parametrize('a,b,c',
                         [(4, 3, 5)])
def test_quadratic_equation_with_uncorrect_data(a, b, c):
    with pytest.raises(Exception):
        quadratic_equation(a, b, c)
