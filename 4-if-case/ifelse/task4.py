"""
Этот модуль содержит функцию, определяющую наименьшее из трех чисел,
а также пример использования данной функции.
"""


def find_smallest_number(num1: float, num2: float, num3: float) -> float:
    """
    Определяет и возвращает наименьшее из 3-х чисел.

    :param num1: 1-ое число
    :type num1: float
    :param num2: 2-ое число
    :type num2: float
    :param num3: 3-е число
    :type num3: float

    :rtype: float
    :return: наименьшее из 3-х чисел
    """
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3


def main() -> None:
    """
    Главная функция, которая запрашивает у пользователя 3 числа
    и выводит наименьшее из них.

    :rtype: None
    :return: None
    """
    while True:
        try:
            first_number, second_number, third_number = map(
                float,
                input('Введите 3 числа через пробел: ').split()
            )
        except Exception as e:
            print(f'{e}. Попробуйте еще раз...')
        else:
            print('Наименьшее: ',
                  find_smallest_number(first_number, second_number, third_number))


if __name__ == '__main__':
    main()