"""
Этот модуль содержит функцию определения наибольшего и наименьшего
числа, а также пример использования данной функции.
"""

from typing import Dict


def largest_and_smallest_numbers(num1: float, num2: float) -> Dict[float, float]:
    """
    Вычисляет и возвращает наибольшее и наименьшее число из двух.

    :param num1: 1-ое число
    :type num1: float
    :param num2: 2-ое число
    :type num2: float

    :rtype: Dict[float, float]
    :return: словарь, содержащий наибольшее и наименьшее числа
    """
    if num1 > num2:
        result = {'min': num2, 'max': num1}
    else:
        result = {'min': num1, 'max': num2}
    return result



def main() -> None:
    """
    Главная функция, которая запрашивает у пользователя 2 числа,
    определяет наибольшее и наименьшее и выводит результат.

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
            print(f'{e}. Попробуй еще раз...')
        else:
            numbers = largest_and_smallest_numbers(first_number, second_number)
            print(f'Наибольшее: {numbers['max']}\nНаименьшее: {numbers['min']}')


if __name__ == '__main__':
    main()