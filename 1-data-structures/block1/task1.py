"""
Этот модуль содержит функцию для вычисления периметра, на основе
стороны квадрата, а также пример использования данной функции.
"""

def calculate_square_perimeter(side_length: float) -> float:
    """
    Вычисляет периметр квадрата.

    :param side_length: сторона квадрата
    :type side_length: float

    :rtype: float
    :return: периметр квадрата

    :raises ValueError: если сторона меньше 0
    """
    if side_length < 0:
        raise ValueError('Сторона не может быть меньше 0.')
    return 4 * side_length


def main() -> None:
    """
    Основная функция, которая запрашивает у пользователя сторону квадрата,
    вычисляет его периметр и выводит результат.

    :rtype: None
    :return: None
    """
    while True:
        try:
            side_length = float(input('Введите сторону квадрата: '))
            perimeter = calculate_square_perimeter(side_length)
        except ValueError as e:
            print(f'{e} Попробуйте снова...')
        else:
            print(f'Периметр = {perimeter}')


if __name__ == '__main__':
    main()
