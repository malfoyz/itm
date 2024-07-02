"""
Этот модуль содержит функцию подсчета квадратов чисел,
а также пример ее использования.
"""

from typing import List


def calculate_squares_of_numbers(min: int = 1, max: int = 10) -> List[int]:
    """
    Вычисляет и возвращает квадраты для чисел от min до max.

    :param min: первое число, с которого начинается подсчет
    :type min: int, default 1
    :param max: последнее число, на котором заканчивается подсчет
    :type max: int, default 10

    :rtype: List[int]
    :return: список, состоящий из квадратов чисел
    """
    if max < min:
        raise Exception('min должен быть меньше, чем max')
    return [x ** 2 for x in range(min, max+1)]


def main() -> None:
    """
    Главная функция, которая выводит квадраты для чисел от 1 до 10.

    :rtype: None
    :return: None
    """
    try:
        squares = calculate_squares_of_numbers(1, 10)
    except Exception as e:
        print(e)
    else:
        for x in squares:
            print(x)


if __name__ == '__main__':
    main()