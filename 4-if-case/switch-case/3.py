"""
Этот модуль содержит функцию, определяющую следующую дату,
а также пример использования данной функции.
"""

from typing import Tuple


def next_date(month: int, day: int) -> Tuple[int, int]:
    """
    Определяет дату, следующую после даты day month

    :param month: месяц
    :type month: int
    :param day: день
    :type day: int

    :rtype: Tuple[int, int]
    :return: следующая дата после даты day month
    """
    if month < 1 or month > 12:
        raise Exception('Месяц не может быть меньше 1 или больше 12.')
    if day < 1 or day > 31:
        raise Exception('День не может быть меньше 1 или больше 31.')

    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12 as m:
            if day == 31:
                day = 1
                month = 1 if month == 12 else month + 1
            else:
                day += 1
        case 4 | 6 | 9 | 11 as m:
            if day == 30:
                day = 1
                month += 1
            else:
                day += 1
        case 2 as m:
            if day == 28:
                day = 1
                month += 1
            else:
                day += 1
    return month, day


def main() -> None:
    """
    Главная функция, которая запрашивает у пользователя день и месяц,
    и выводит дату следующего за ними дня.

    :rtype: None
    :return: None
    """
    while True:
        try:
            day, month = map(
                int,
                input('Введите день и месяц через точку (Например: 3.10) : ').split('.')
            )
            month, day = next_date(month, day)
            print(f'Следующая дата: {day}.{month}')
        except Exception as e:
            print(f'{e}. Попробуйте еще раз...')


if __name__ == '__main__':
    main()
