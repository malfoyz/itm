import pytest

from ifelse.task5 import identify_quarter


@pytest.mark.parametrize('x,y,expected_result',
                         [(10, 10, 1),
                          (-2, 3, 2),
                          (-5, -20, 3),
                          (20, -14, 4)])
def test_identify_quarter(x, y, expected_result):
    assert identify_quarter(x, y) == expected_result