import pytest

from block6.task2 import bubble_sort


@pytest.mark.parametrize('arr,expected_result',
                         [([10, 9, 8, 7], [7, 8, 9, 10]),
                          ([0, 0, 1, 0, 3], [0, 0, 0, 1, 3]),
                          ([-3, -10, -3, -2], [-10, -3, -3, -2])])
def test_bubble_sort(arr, expected_result):
    assert bubble_sort(arr) == expected_result
