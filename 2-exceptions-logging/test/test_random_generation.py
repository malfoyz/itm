import pytest

from logging_tasks.homework.random_generation import random_generation


@pytest.mark.parametrize('min,max,count,expected_result',
                         [(10, 20, 3, 3),
                          (3, 3, 10, 10),
                          (1, 500, 100, 100)])
def test_random_generation_with_correct_data(min, max, count, expected_result):
    assert len(random_generation(min, max, count)) == expected_result


@pytest.mark.parametrize('min,max,count',
                         [(-3, 10, 5),
                          (10, 20, -10)])
def test_random_generation_with_uncorrect_data(min, max, count):
    with pytest.raises(Exception):
        random_generation(min, max, count)
