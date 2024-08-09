"""
Этот модуль содержит ...
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Абстратный класс животного"""

    @abstractmethod
    def voice(self):
        """Возвращает звучание животного"""
        pass


class Cat(Animal):
    """Класс кота"""

    def voice(self):
        """Возвращает звучание кота"""
        return 'Мяу'


class Dog(Animal):
    """Класс собаки"""

    __instance = None

    def __init__(self, name: str):
        self.__name = name

        if Dog.__instance is None:
            Dog.__instance = self
        else:
            raise Exception('Вы не можете создать другой объект, пока существует один из них.')

    @staticmethod
    def get_instance():
        if not Dog.__instance:
            Dog()
        return Dog.__instance

    def voice(self):
        """Возвращает звучание собаки"""
        return 'Гав'


def main() -> None:
    dog = Dog('Алекс')
    print(dog)

    same_dog = Dog.get_instance()
    print(same_dog)

    # new_dog = Dog()


if __name__ == '__main__':
    main()
