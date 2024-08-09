"""
Этот модуль содержит функцию нахождения простых чисел,
а также пример ее использования.
"""

from typing import List


def find_prime_numbers(min: int = 2, max: int = 50) -> List[int]:
    """
    Ищет список простых чисел от min до max.

    :param min: число, с которого начинается поиск
    :type min: int, default 2
    :param max: число, на котором заканчивается поиск
    :type max: int, default 50

    :rtype: List[int]
    :return: список, состоящий из простых чисел
    """
    if min < 2:
        raise Exception('min не может быть меньше 2')
    if max < 2:
        raise Exception('max не может быть меньше 2')
    if max < min:
        raise Exception('max не может быть меньше, чем min')

    prime_numbers = []
    for i in range(min, max+1):
        is_prime = True
        for j in range(2, i+1):
            if i != j and i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)

    return prime_numbers


def main() -> None:
    """
    Главная функция, которая выводит список простых чисел от 2 до 50.

    :rtype: None
    :return: None
    """
    try:
        prime_numbers = find_prime_numbers(30, 50)
    except Exception as e:
        print(e)
    else:
        print(prime_numbers)


if __name__ == '__main__':
    main()