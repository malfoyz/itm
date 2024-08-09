import pytest

from block2.task1 import convert_sm_to_meters


@pytest.mark.parametrize('length,expected_result',
                         [(100, 1),
                          (0, 0),
                          (402, 4)])
def test_convert_sm_to_meters(length, expected_result):
    assert convert_sm_to_meters(length) == expected_result