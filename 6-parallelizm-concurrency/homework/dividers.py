"""
Дано число в диапазоне от 1_000_000 до 20_000_000.
Получите список целочисленных делителей этого числа.
"""

import multiprocessing

from typing import List


def get_dividers(number: int, start: int, end: int) -> List[int]:
    """
    Находит и возвращает список делителей числа в заданном диапазоне.

    :param number: число, количество делителей которого нужно найти
    :type number: int
    :param start: начало диапазона
    :type start: int
    :param end: конец диапазона
    :type end: int

    :return: список делителей в заданном диапазоне
    :rtype: List[int]

    :raises TypeError: если тип одного из параметров отличается от int
    :raises ValueError: если параметр number не вмещается в диапазон между 1000000 и 20000000
    :raises ValueError: если start > end
    """

    if not isinstance(number, int):
        raise TypeError('Параметр number должен представлять тип int')
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError('Параметры start и end должны представлять тип int')
    if number < 1000000 or number > 20000000:
        raise ValueError('Число должно быть в дипазаоне от 1.000.000 до 20.000.000')
    if start >= end:
        raise ValueError('Параметр end должен быть больше или равен start')

    dividers = []
    for i in range(start, end + 1):
        if number % i == 0:
            dividers.append(i)
    print(dividers)
    return dividers


def get_dividers_with_mulptiprocessing(number: int) -> List[int]:
    """
    Находит и возвращает список делителей числа, используя многопроцессорность.

    :param number: число, количество делителей которого нужно найти
    :type number: int

    :return: список делителей числа
    :rtype: List[int]

    :raises TypeError: если тип параметра number отличается от int
    :raises ValueError: если параметр number не вмещается в диапазон между 1000000 и 20000000
    :raises Exception: если возникнет ошибка в функции get_dividers
    """
    if not isinstance(number, int):
        raise TypeError('Параметр number должен представлять тип int')
    if number < 1000000 or number > 20000000:
        raise ValueError('Число должно быть в дипазаоне от 1.000.000 до 20.000.000')

    processes_count = multiprocessing.cpu_count()         # число процессов = число доступных ядер

    step = number // processes_count          # шаг для каждого процесса
    tasks = [(number, i, min(i + step, number)) for i in range(1, number, step)]

    with multiprocessing.Pool(processes_count) as pool:
        try:
            results = pool.starmap(get_dividers, tasks)
        except Exception as e:
            print(f'Ошибка: {e}')
            return []

    dividers = []
    for result in results:
        dividers.extend(result)

    return dividers


def main() -> None:
    while True:
        try:
            number = int(input('Введите число в диапазоне от 1.000.000 до 20.000.000: '))
            dividers = get_dividers_with_mulptiprocessing(number)
        except Exception as e:
            print(f'{e}. Попробуйте снова...')
        else:
            print('Делители числа:', dividers)


if __name__ == '__main__':
    main()