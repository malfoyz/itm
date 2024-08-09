"""
Этот модуль содержит классы транспортного средства, машины, мопеда,
а также пример использования данных классов.
"""


class MeansOfTransport:
    """Класс транспортного средства"""

    def __init__(self, color: str, brand: str):
        self.color = color
        self.brand = brand

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    def show_color(self) -> None:
        """Выводит на печать цвет ТС."""
        print(f'Цвет ТС: {self.__color}')

    def show_brand(self) -> str:
        """Возвращает марку ТС."""
        return self.__brand


class Car(MeansOfTransport):
    """Класс машины"""

    car_drive: int = 4

    def __new__(cls, *args, **kwargs):
        print('вызов __new__ для ' + str(cls))
        return super().__new__(cls)

    def __init__(self, color: str, brand: str, wheels_count: int, places_count: int,
                 year: int, length: float = 300.0, min_speed: float = 0.0,
                 max_speed: float = 240.0, step: float = 10.0):
        self.__wheels_count = wheels_count
        self._places_count = places_count
        self.__year = year
        self.__min_temperature = -40
        self.__length = length
        self.values = [1, 2, 3, 4, 5]

        self.min_speed = min_speed
        self.max_speed = max_speed
        self.step = step
        super().__init__(color, brand)


    def __call__(self, *args, **kwargs):
        print('__call__')
        self.__year = args[0]
        return self.__year

    def __del__(self):
        print('Удаление экземпляра: ' + str(self))

    def __getattribute__(self, item):  # вызывается при считывании аттрибута через экземпляр класса
        if item == 'year':
            raise ValueError('Доступ запрещен')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):    # вызыывается при установке новых атрибутов, в т.ч. в __init__
        if key == 'human':
            raise AttributeError('Недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):         # вызывается при удалении атрибута из экземпляра класса
        print('__delattr__: ' + item)
        object.__delattr__(self, item)

    def __getattr__(self, item):         # вызывается автоматически, когда идет обращение к несуществующему атрибуту экземпляра класса
        print('__getattr__: ' + item)

    def __len__(self):
        return self.__year

    def __bool__(self):
        return self.__wheels_count == self._places_count

    def __abs__(self):
        return abs(self.__min_temperature)

    @classmethod
    def __verify_length(cls, other):
        if not isinstance(other, (float, Car)):
            raise TypeError('Операнд должен быть тип float или Car')

        return other if isinstance(other, float) else other.__length

    def __add__(self, other):
        length = self.__verify_length(other)
        return Car(self.__length + length)

    def __radd__(self, other):  # сложение, когда объект класса справа от знака +
        return self + other

    def __iadd__(self, other):
        length = self.__verify_length(other)
        self.__length += length

    def __sub__(self, other):
        length = self.__verify_length(other)
        return Car(self.__length - length)

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        length = self.__verify_length(other)
        self.__length -= length

    def __mul__(self, other):
        length = self.__verify_length(other)
        return Car(self.__length * length)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        length = self.__verify_length(other)
        self.__length *= length

    def __truediv__(self, other):
        length = self.__verify_length(other)
        return Car(self.__length / length)

    def __rtruediv__(self, other):
        return self / other

    def __itruediv__(self, other):
        length = self.__verify_length(other)
        self.__length /= length

    def __floordiv__(self, other):
        length = self.__verify_length(other)
        self.__length //= length

    def __rfloordiv__(self, other):
        return self // other

    def __ifloordiv__(self, other):
        length = self.__verify_length(other)
        self.__length //= length

    def __mod__(self, other):
        length = self.__verify_length(other)
        self.__length %= length

    def __rmod__(self, other):
        return self % other

    def __imod__(self, other):
        length = self.__verify_length(other)
        self.__length %= length

    def __pow__(self, other):
        length = self.__verify_length(other)
        return Car(self.__length ** length)

    def __rpow__(self, other):  # сложение, когда объект класса справа от знака +
        return self ** other

    def __ipow__(self, other):
        length = self.__verify_length(other)
        self.__length **= length

    def __eq__(self, other):
        length = self.__verify_length(other)
        return self.brand == other.brand and self.year == other.year

    def __hash__(self):
        return hash((self.brand, self.year))

    def __lt__(self, other):
        length = self.__verify_length(other)
        return self.__length < length

    def __gt__(self, other):
        length = self.__verify_length(other)
        return self.__length > length

    def __le__(self, other):
        length = self.__verify_length(other)
        return self.__length <= length

    def __getitem__(self, item):
        if 0 <= item <= len(self.values):
            return self.values[item]
        else:
            raise IndexError('Неверный индекс')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Индекс должен быть целым неотрицательным числом')

        if key >= len(self.values):
            off = key + 1 - len(self.values)
            self.values.extend([None] * off)

        self.values[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым неотрицательным числом')

        del self.values[key]

    def __iter__(self):
        self.current_speed = self.min_speed - self.step
        return self

    def __next__(self):
        if self.current_speed + self.step <= self.max_speed:
            self.current_speed += self.step
            return self.current_speed
        else:
            raise StopIteration

    def __repr__(self):   # отладочная инфа
        return f'{self.__class__}: {self.brand}'

    def __str__(self):    # для пользователя, выводится в print() и str()
        return f'{self.brand}'

    @classmethod
    def get_drive(cls):
        """Возвращает число приводов машины"""
        return cls.car_drive


class Moped(MeansOfTransport):
    """Класс мопеда"""

    def __init__(self, color: str, brand: str, wheels_count: int):
        self.__wheels_count = wheels_count
        super().__init__(color, brand)

    @staticmethod
    def get_time(distance: float, max_speed: float) -> float:
        """Возвращает время, за которое мопед проедет расстояние distance при скорости max_speed"""
        if not isinstance(distance, (int, float)) or not isinstance(max_speed, (int, float)):
            raise TypeError('Расстояние и максимальная скорость должны быть целыми или вещественными числами')

        return distance / max_speed



def main():
    car = Car('red', 'VAZ', 4, 5, 1992)
    print(car._places_count)
    # print(car.__year)    Ошибка
    print(car._Car__year)  # не рекомендуется

    print(Car.get_drive())

    car(2000)
    print(car._Car__year)

    for speed in car:
        print(speed, end=' ')
    print()


if __name__ == '__main__':
    main()