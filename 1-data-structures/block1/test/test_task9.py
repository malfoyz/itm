import pytest

from block1.task9 import calculate_geometric_mean


@pytest.mark.parametrize('a,b,expected_result',
                         [(110, 220, 155.56349186104046),
                          (0, 0, 0),
                          (5.2, 20.4, 10.299514551666986)])
def test_calculate_geometric_mean(a, b, expected_result):
    assert calculate_geometric_mean(a, b) == expected_result