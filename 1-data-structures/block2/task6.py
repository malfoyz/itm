"""
Этот модуль содержит функцию вычисления левой и правой цифр в двузначном
числе, а также пример использования данной функции.
"""

from typing import Tuple


def calculate_digits(number: int) -> Tuple[int, int]:
    if number < 10 or number > 99:
        raise ValueError('Число должно быть двузначным!')
    return number // 10, number % 10


def main() -> None:
    while True:
        try:
            number = int(input('Введите двузначное число: '))
            left_digit, right_digit = calculate_digits(number)
        except ValueError as e:
            print(f'{e}. Попробуйте снова...')
        else:
            print(f'Левая цифра = {left_digit}, правая цифра = {right_digit}')


if __name__ == '__main__':
    main()