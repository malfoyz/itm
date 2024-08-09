import pytest

from homework.animals import Animal, Cat, Dog


class TestCat:
    def test_voice_method(self):
        cat = Cat()
        assert cat.voice() == 'Мяу'

    def test_inheritance(self):
        cat = Cat()
        assert isinstance(cat, Animal)


class TestDog:
    def test_voice_method(self):
        dog = Dog('Max')
        assert dog.voice() == 'Гав'

    def test_get_instance_method(self):
        assert Dog.get_instance()

    def test_inheritance(self):
        dog = Dog.get_instance()
        assert isinstance(dog, Animal)

    def test_singleton_exception(self):
        with pytest.raises(Exception):
            Dog('Alex')
