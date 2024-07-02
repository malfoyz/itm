"""
Этот модуль содержит функцию вывода таблицы умножения,
а также пример использования данной функции.
"""

def print_multiplication_table(start: int, stop: int) -> None:
    """
    Выводит таблицу унможения.

    :param start: первое число таблицы умножения
    :type start: int
    :param stop: последнее число таблицы умножения
    :type stop: int

    :rtype: None
    :return: None
    """
    if start < stop:
        raise Exception('start должен быть меньше stop')

    print(' ' * 3, end='')
    for i in range(start, stop+1):
        print(f'{i:4}', end='')
    print('\n', ' ' * 3, end='', sep='')
    for i in range(start, stop+1):
        print(f'{"-":>4}', end='')
    print()

    for i in range(start, stop+1):
        print(i, '|', end='')
        for j in range(start, stop+1):
            print(f'{i * j:4}', end='')
        print()


def main() -> None:
    """
    Главная функция, вызывающая функцию таблицы унможения.

    :rtype: None
    :return: None
    """
    try:
        print_multiplication_table(1, 9)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
