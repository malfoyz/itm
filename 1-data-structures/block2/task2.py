"""
Этот модуль содержит функцию перевода массы из кг в тонны,
а также пример использования данной функции.
"""


def convert_kg_to_tons(mass: int) -> int:
    return mass // 1000


def main() -> None:
    while True:
        try:
            kg = int(input('Введите массу (в кг): '))
        except ValueError as e:
            print(f'{e} Попробуйте снова...')
        else:
            tons = convert_kg_to_tons(kg)
            print(f'Кол-во полных тонн = {tons}')


if __name__ == '__main__':
    main()