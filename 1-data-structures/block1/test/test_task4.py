import pytest

from block1.task4 import calculate_circle_length


@pytest.mark.parametrize('radius,expected_result',
                         [(3, 9.42), (0, 0), (4.5, 14.13)])
def test_calculate_circle_length(radius, expected_result):
    assert calculate_circle_length(radius) == expected_result


@pytest.mark.parametrize('radius',
                         [-2, -4.5])
def test_calculate_circle_length_with_negative_radius(radius):
    with pytest.raises(ValueError):
        calculate_circle_length(radius)