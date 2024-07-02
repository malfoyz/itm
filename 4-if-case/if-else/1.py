"""
Этот модуль содержит функцию нахождения положительных чисел в списке,
а также пример использования данной функции.
"""

from typing import List


def find_positive_numbers_count(nums: List[int]) -> int:
    """
    Находит и возвращает кол-во целых чисел среди чисел num1, num2, num3.

    :param nums: список, состоящий из целых чисел
    :type nums: int

    :rtype: int
    :return: кол-во целых чисел
    """
    return len([i for i in nums if i > 0])


def main() -> None:
    """
    Главная функция, которая предлагает пользователю ввести 3 числа,
    затем находит кол-во положительных чисел среди них.

    :rtype: None
    :return: None
    """
    while True:
        try:
            numbers = list(map(
                int,
                input('Введите 3 целых числа через пробел: ').split()
            ))
            if len(numbers) != 3:
                raise Exception('Необходимо ввести именно 3 числа.')
        except Exception as e:
            print(f'{e}. Попробуйте заново...')
        else:
            print('Кол-во положительных чисел = ',
                  find_positive_numbers_count(numbers))


if __name__ == '__main__':
    main()