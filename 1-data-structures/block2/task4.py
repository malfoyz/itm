"""
Этот модуль содержит функцию вычисления числа отрезков A в отрезке B,
а также пример использования данной функции.
"""


def calcualte_subsections_count(section_len: int, subsection_len: int) -> int:
    if subsection_len == 0:
        raise ZeroDivisionError('Отрезок B не должен быть равен 0.')
    return section_len // subsection_len


def main() -> None:
    while True:
        try:
            A, B = map(
                int,
                input('Введите длины отрезков A и B через пробел (A > B): ')
                .split()
            )
            subsections_count = calcualte_subsections_count(A, B)
        except ValueError as e:
            print(f'{e} Попробуйте снова...')
        else:
            print(f'Кол-во отрезков B, размещенных на отрезке A = {subsections_count}')


if __name__ == '__main__':
    main()