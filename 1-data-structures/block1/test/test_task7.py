import pytest

from block1.task7 import calculate_circle_length_area


@pytest.mark.parametrize('radius,expected_result',
                         [(3, (18.84, 28.26)),
                          (0, (0, 0)),
                          (4.5, (28.26, 63.585))])
def test_calculate_circle_length_area(radius, expected_result):
    assert calculate_circle_length_area(radius) == expected_result


@pytest.mark.parametrize('radius',
                         [(-2),
                          (-4.5)])
def test_calculate_circle_length_area(radius):
    with pytest.raises(ValueError):
        calculate_circle_length_area(radius)