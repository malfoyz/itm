"""
Этот модуль содержит функцию вычисления остатка отрезка B на отрезке A,
а также пример использования данной функции.
"""


def calculate_section_remains(section: int, subsection: int) -> int:
    return section % subsection


def main() -> None:
    while True:
        try:
            A, B = map(
                int,
                input('Введите длины отрезков A и B через пробел (A > B): ')
                .split()
            )
        except ValueError as e:
            print(f'{e} Попробуйте снова...')
        else:
            remains = calculate_section_remains(A, B)
            print(f'Остаток отрезка B на отрезке A = {remains}')


if __name__ == '__main__':
    main()