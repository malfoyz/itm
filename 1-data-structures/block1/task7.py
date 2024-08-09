"""
Этот модуль содержит функцию вычисления длины окружности и площади круга,
а также пример использования данной функции.
"""

from typing import Tuple


PI = 3.14


def calculate_circle_length_area(radius: float) -> Tuple[float, float]:
    if radius < 0:
        raise ValueError('Радиус не может быть меньше 0.')
    length = 2 * PI * radius
    surface_area = PI * radius ** 2
    return length, surface_area


def main() -> None:
    while True:
        try:
            radius = float(input('Введите радиус круга: '))
            length, surface_area = calculate_circle_length_area(radius)
        except ValueError as e:
            print(f'{e}. Попробуйте снова...')
        else:
            print(f'Длина окружности = {length}, Площадь круга = {surface_area}')


if __name__ == '__main__':
    main()