import pytest

from block1.task3 import calculate_rect_area_and_perimeter


@pytest.mark.parametrize('a,b,expected_result',
                         [(2, 2, (4, 8)),
                          (0, 0, (0, 0)),
                          (10.5, 5.5, (57.75, 32.0))])
def test_calculate_rect_area_and_perimeter(a, b, expected_result):
    assert calculate_rect_area_and_perimeter(a, b) == expected_result


@pytest.mark.parametrize('a,b',
                         [(-2, -2),
                          (-2, 6),
                          (8, -2)])
def test_calculate_rect_area_and_perimeter_with_negative_numbers(a, b):
    with pytest.raises(ValueError):
        calculate_rect_area_and_perimeter(a, b)