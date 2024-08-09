"""
Этот модуль содержит функцию вычисления площади и периметра прямоугольника,
а также пример использования данной функции.
"""

from typing import Tuple


def calculate_rect_area_and_perimeter(a: float, b: float) -> Tuple[float, float]:
    """
    Вычисляет площадь и периметр прямоугольника.

    :param a: первая сторона прямоугольника
    :type a: float
    :param b: вторая сторона прямоугольника
    :type b: float

    :rtype: Tuple[float, float]
    :return: кортеж, содержащий площадь и периметр прямоугольника

    :raises ValueError: если любая из сторон меньше 0
    """
    if a < 0 or b < 0:
        raise ValueError('Стороны должны быть больше 0.')
    area = a * b
    perimeter = 2 * (a + b)
    return area, perimeter


def main() -> None:
    """
    Основная функция, которая запрашивает у пользователя стороны
    прямоуольника, вычисляет его площадь и периметр и выводит результат.

    :rtype: None
    :return: None
    """
    while True:
        try:
            a, b = map(float, input('Введите стороны прямоугольника через пробел: ').split())
            area, perimeter = calculate_rect_area_and_perimeter(a, b)
        except ValueError as e:
            print(f'{e}. Попробуйте снова...')
        else:
            print(f'Площадь = {area}, Периметр = {perimeter}')


if __name__ == '__main__':
    main()