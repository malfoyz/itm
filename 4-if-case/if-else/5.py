"""
Этот модуль содержит функцию, определяющую номер четверти по координатам
четверти, а также пример использования данной функции.
"""


def identify_quarter(x: float, y: float) -> int:
    """
    Определяет и возвращает номер четверти, которой принадлежат координаты.

    :param x: координата OX
    :type x:  float
    :param y: координата OY
    :type y: float

    :rtype: int
    :return: номер четверти, которой принадлежат координаты x и y
    """
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


def main() -> None:
    """
    Главная функция, которая запрашивает у пользователя координаты
    x и y и выводит номер четверти, которым они принадлежат.

    :rtype: None
    :return: None
    """
    while True:
        try:
            x, y = map(
                float,
                input('Введите координаты точки X и Y через пробел: ').split()
            )
        except Exception as e:
            print(f'{e}. Попробуйте еще раз...')
        else:
            print(f'Точка ({x}, {y}) попала в четверть №{identify_quarter(x, y)}')


if __name__ == '__main__':
    main()