import pytest

from switchcase.task1 import assessment_description


@pytest.mark.parametrize('assessment,expected_result',
                         [(1, 'Плохо!'),
                          (2, 'Неудовлетворительно!'),
                          (3, 'Удовлетворительно!'),
                          (4, 'Хорошо!'),
                          (5, 'Отлично!'),
                          (7, 'Ошибка!')])
def test_assessment_description(assessment, expected_result):
    assert assessment_description(assessment) == expected_result