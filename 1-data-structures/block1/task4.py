"""
Этот модуль содержит функцию вычисления длины окружности,
а также пример использования данной функции.
"""


PI = 3.14


def calculate_circle_length(radius: float) -> float:
    if radius < 0:
        raise ValueError('Радиус не может быть меньше 0.')
    return PI * radius


def main() -> None:
    while True:
        try:
            radius = float(input('Введите радиус окружности'))
            length = calculate_circle_length(radius)
        except ValueError as e:
            print(f'{e} Попробуйте снова...')
        else:
            print(f'Длина окружности = {length}')


if __name__ == '__main__':
    main()