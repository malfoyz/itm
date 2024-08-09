"""
Этот модуль содержит функцию вычисления объёма и площади поверхности прамоугольного
параллепипеда, а также пример использования данной функции.
"""

from typing import Tuple


def calculate_rect_parallelepiped_volume_area(a: float, b: float, c: float) -> Tuple[float, float]:
    if a < 0 or b < 0 or c < 0:
        raise ValueError('Стороны должны быть больше 0.')
    volume = a * b * c
    surface_area = 2 * (a * b + b * c + a * c)
    return volume, surface_area


def main() -> None:
    while True:
        try:
            a, b, c = map(
                float,
                input('Введите длины ребер a, b, c прямоугольного параллепипеда через пробел: ')
                .split()
            )
            volume, surface_area = calculate_rect_parallelepiped_volume_area(a, b, c)
        except ValueError as e:
            print(f'{e}. Попробуйте снова...')
        else:
            print(f'Объем = {volume}, Площадь поверхности = {surface_area}')


if __name__ == '__main__':
    main()