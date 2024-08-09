"""
Этот модуль содержит функцию передода расстояния в метрах в сантиметры,
а также пример использования данной функции.
"""


def convert_sm_to_meters(length: int) -> int:
    return length // 100


def main() -> None:
    while True:
        try:
            sm = int(input('Введите расстояние (в см): '))
        except ValueError as e:
            print(f'{e}. Попробуйте снова...')
        else:
            meters = convert_sm_to_meters(sm)
            print(f'Расстояние в метрах = {meters}')


if __name__ == '__main__':
    main()
