import pytest

from block2.task5 import calculate_section_remains


def test_calculate_section_remains():
    assert calculate_section_remains(100, 13) == 9


def test_calculate_section_remains_with_zero():
    with pytest.raises(ZeroDivisionError):
        calculate_section_remains(100, 0)