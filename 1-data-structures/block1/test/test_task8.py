import pytest

from block1.task8 import calculate_arifmethic_mean


@pytest.mark.parametrize('a,b,expected_result',
                         [(3, 4, 3.5),
                          (0, 0, 0),
                          (4.2, 3.8, 4)])
def test_calculate_arifmethic_mean(a, b, expected_result):
    assert calculate_arifmethic_mean(a, b) == expected_result