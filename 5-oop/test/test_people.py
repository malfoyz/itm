import pytest

from homework.people import HumanList


class TestHumanList:
    def test_iterator(self):
        initial = ['Max', 'Alex', 'Miley']
        human_list = HumanList(initial)
        result = []
        for human in human_list:
            result.append(human)
        assert result == initial

    def test_append_not_str(self):
        human_list = HumanList([])
        with pytest.raises(TypeError):
            human_list.append(123)
