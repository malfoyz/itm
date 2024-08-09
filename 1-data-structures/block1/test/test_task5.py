import pytest

from block1.task5 import calculate_cube_volume_and_area


@pytest.mark.parametrize('edge_length,expected_result',
                         [(3, (27, 54)),
                          (0, (0, 0)),
                          (4.5, (91.125, 121.5))])
def test_calculate_cube_volume_and_area(edge_length, expected_result):
    assert calculate_cube_volume_and_area(edge_length) == expected_result


@pytest.mark.parametrize('edge_length',
                         [-2, -4.5])
def test_calculate_cube_volume_and_area(edge_length):
    with pytest.raises(ValueError):
        calculate_cube_volume_and_area(edge_length)