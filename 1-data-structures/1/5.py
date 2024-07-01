"""
Этот модуль содержит функцию для вычисления объема и площади поверхности
куба, а также пример использования данной функции.
"""

from typing import Tuple

def calculate_cube_volume_and_area(edge_length: float) -> Tuple[float, float]:
    """
    Вычисляет и возвращает объем и площадь поверхности куба.

    :param edge_length: длина ребра куба
    :type edge_length: float

    :rtype: Tuple[float, float]
    :return: кортеж, содержащий объем и плозадь повехрности куба
    """
    volume = edge_length ** 3
    area = 6 * edge_length ** 2
    return volume, area


def main():
    """
    Основная функция, которая запрашивает у пользователя длину ребра куба,
    вычисляет объем и площадь поверхности куба и выводит результат.

    :rtype: None
    :return: None
    """
    edge_length = float(input('Введите длину ребра куба: '))
    volume, area = calculate_cube_volume_and_area(edge_length)
    print(f'Объем куба = {volume}, Площадь поверхности = {area}')


if __name__ == '__main__':
    main()