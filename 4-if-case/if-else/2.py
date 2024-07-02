"""
Этот модуль содержит функцию вычисления наибольшего числа из двух,
а также пример использования данной функции.
"""


def largest_number(num1: float, num2: float) -> float:
    """
    Вычисляет и возвращает наибольшее число из двух.

    :param num1: 1-ое число
    :type num1: float
    :param num2: 2-ое число
    :type num2: float

    :rtype: float
    :return: наибольшее число
    """
    return num1 if num1 > num2 else num2


def main() -> None:
    """
    Главная функция, которая запрашивает у пользователя 2 числа и
    выводит наибольшее из них.

    :rtype: None
    :return: None
    """
    while True:
        try:
            first_number, second_number = map(
                float,
                input('Введите 2 числа через пробел: ').split()
            )
        except Exception as e:
            print(f'{e}. Попробуйте еще раз...')
        else:
            print('Наибольшее число: ',
                  largest_number(first_number, second_number))


if __name__ == '__main__':
    main()