"""
Этот модуль содержит функцию вычисления среднего арифметического двух чисел,
а также пример использования данной функции.
"""


def calculate_arifmethic_mean(a: float, b: float) -> float:
    return (a + b) / 2


def main() -> None:
    while True:
        try:
            a, b = map(float, input('Введите 2 числа через пробел: ').split())
        except ValueError as e:
            print(f'{e}. Попробуйте снова...')
        else:
            arifm_mean = calculate_arifmethic_mean(a, b)
            print(f'Среднее арифметическое = {arifm_mean}')


if __name__ == '__main__':
    main()