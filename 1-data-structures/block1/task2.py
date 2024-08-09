"""
Этот модуль содержит функцию для вычисления площади квадрата на
основе стороны квадрата, а также пример использования этой функции.
"""

def calculate_square_area(side_length: float) -> float:
    """
    Вычисляет площадь квадрата.

    :param side_length: сторона квадрата
    :type side_length: float

    :rtype: float
    :return: площадь квадрата

    :raises ValueError: если сторона меньше 0
    """
    if side_length < 0:
        raise ValueError('Сторона должна быть больше 0.')
    return side_length ** 2


def main() -> None:
    """
    Основная функция, которая запрашивает у пользователя сторону квадрата,
    вычисляет его площадь и выводит результат.

    :rtype: None
    :return: None
    """
    while True:
        try:
            side_length = float(input('Введите сторону квадрата:'))
            area = calculate_square_area(side_length)
        except ValueError as e:
            print(f'{e} Попробуйте снова...')
        else:
            print(f'Площадь = {area}')


if __name__ == '__main__':
    main()
