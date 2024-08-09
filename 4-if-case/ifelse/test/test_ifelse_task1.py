import pytest

from ifelse.task1 import find_positive_numbers_count


@pytest.mark.parametrize('nums,expected_result',
                         [([-3, -2, -1], 0),
                          ([-3, 2, 1], 2),
                          ([0, 0, 0], 0)])
def test_find_positive_numbers_count(nums, expected_result):
    assert find_positive_numbers_count(nums) == expected_result