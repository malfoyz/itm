"""
Этот модуль содержит функцию вычисления среднего геометрического,
двух чисел, а также пример использования данной функции.
"""


def calculate_geometric_mean(a: float, b: float) -> float:
    return (a * b) ** 0.5


def main() -> None:
    while True:
        try:
            a, b = map(float, input('Введите 2 неотриц. числа: ').split())
        except ValueError as e:
            print(f'{e}. Попробуйте снова...')
        else:
            geometric_mean = calculate_geometric_mean(a, b)
            print(f'Среднее геометрическое = {geometric_mean}')


if __name__ == '__main__':
    main()