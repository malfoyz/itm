import pytest

from block2.task4 import calcualte_subsections_count


def test_calcualte_subsections_count():
    assert calcualte_subsections_count(100, 13) == 7


def test_calcualte_subsections_count_with_zero():
    with pytest.raises(ZeroDivisionError):
        calcualte_subsections_count(100, 0)