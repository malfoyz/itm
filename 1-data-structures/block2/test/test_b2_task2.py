import pytest

from block2.task2 import convert_kg_to_tons


@pytest.mark.parametrize('mass,expected_result',
                         [(1000, 1),
                          (0, 0),
                          (4002, 4)])
def test_convert_kg_to_tons(mass, expected_result):
    assert convert_kg_to_tons(mass) == expected_result