import pytest

from block2.task3 import convert_bytes_to_kilobytes


@pytest.mark.parametrize('bytes,expected_result',
                         [(1024, 1),
                          (0, 0),
                          (7654, 7)])
def test_convert_bytes_to_kilobytes(bytes, expected_result):
    assert convert_bytes_to_kilobytes(bytes) == expected_result