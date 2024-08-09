import pytest

from block6.task1 import binary_search


@pytest.mark.parametrize('arr,target,expected_result',
                         [([2, 3, 4, 10, 40], 4, 2),
                         ([2, 3, 2, 3], 3, 1),
                          ([2, 4, 5, 10], 11, -1)])
def test_binary_search(arr, target, expected_result):
    assert binary_search(arr, target) == expected_result
