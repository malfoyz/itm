"""
Этот модуль содержит ...
"""
class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


from typing import List


class HumanList:
    """Класс, содержащий список людей"""

    def __init__(self, people: List[str]):
        self.__people = list(people)

    def append(self, human: str):
        if not isinstance(human, str):
            raise TypeError('Имя должно быть строкой')

        self.__people.append(human)

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index + 1 < len(self.__people):
            self.index += 1
            return self.__people[self.index]
        else:
            raise StopIteration


def main() -> None:
    people = HumanList(['Алекс', 'Вова'])
    people.append('Серёга')
    for human in people:
        print(human)


if __name__ == '__main__':
    main()