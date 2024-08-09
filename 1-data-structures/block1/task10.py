"""
Этот модуль содержит функцию вычисления арифметических
операций, а также пример использования данной функции.
"""

from typing import Tuple


def calculate_arithmetic_operations(a: float, b: float) -> Tuple[float, float, float, float]:
    if b == 0:
        raise ZeroDivisionError('Деление на 0 невозможно.')
    summ = a + b
    diff = a - b
    comp = a * b
    division = a / b
    return summ, diff, comp, division


def main() -> None:
    while True:
        try:
            a, b = map(float, input('Введите 2 ненулевых числа = ').split())
            summ, diff, comp, division = calculate_arithmetic_operations(a, b)
        except ValueError as e:
            print(f'{e} Попробуйте снова...')
        else:
            print(f'Сумма = {summ}\nРазность = {diff}\nПроизведение = {comp}\nЧастное = {division}')


if __name__ == '__main__':
    main()