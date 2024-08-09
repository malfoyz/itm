import pytest

from block1.task6 import calculate_rect_parallelepiped_volume_area


@pytest.mark.parametrize('a,b,c,expected_result',
                         [(3, 4, 7, (84, 122)),
                          (0, 0, 0, (0, 0)),
                          (4.5, 8.2, 3.1, (114.39, 152.54))])
def test_calculate_rect_parallelepiped_volume_area(a, b, c, expected_result):
    assert calculate_rect_parallelepiped_volume_area(a, b, c) == expected_result


@pytest.mark.parametrize('a,b,c',
                         [(-2, 4, 3),
                          (4, -3, -4.5)])
def test_calculate_rect_parallelepiped_volume_area(a, b, c):
    with pytest.raises(ValueError):
        calculate_rect_parallelepiped_volume_area(a, b, c)