import pytest

from block1.task2 import calculate_square_area


@pytest.mark.parametrize('side_length,expected_result',
                         [(4, 16), (0, 0), (2.5, 6.25)])
def test_calucalte_square_area(side_length, expected_result):
    assert calculate_square_area(side_length) == expected_result


@pytest.mark.parametrize('side_length',
                         [-10, -3.5])
def test_calculate_square_area_with_negative_number(side_length):
    with pytest.raises(ValueError):
        calculate_square_area(side_length)