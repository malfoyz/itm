"""
Этот модуль содержит функцию вычисления факториалов, а также пример
использования данной функции.
"""

from typing import List


def factorials(start: int = 1, stop: int = 5) -> List[int]:
    """
    Вычисляет и возвращает факториалы для чисел от start до stop.

    :param start: первое число, для которого вычисляется факториал
    :type start: int
    :param stop: последнее число, для которого возвращается факториал
    :type stop: int

    :rtype: List[int]
    :return: список, состоящий из факториалов чисел
    """
    if start < 1:
        raise Exception('start должен быть больше либо равен 1.')
    if start > stop:
        raise Exception('start должен быть меньше, чем stop')

    result = []
    for i in range(1, stop+1):
        fact = 1
        for j in range(1, i+1):
            fact *= j
        if i >= start:
            result.append(fact)
    return result


def main() -> None:
    """
    Главная функция, которая выводит факториалы чисел.

    :rtype: None
    :return: None
    """
    try:
        factorials_list = factorials(10, 12)
    except Exception as e:
        print(e)
    else:
        for fact in factorials_list:
            print(fact)


if __name__ == '__main__':
    main()
