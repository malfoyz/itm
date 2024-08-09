"""
Этот модуль содержит функцию перевода размера файла из байт в килобайты,
а также пример использования данной функции.
"""


def convert_bytes_to_kilobytes(bytes: int) -> int:
    return bytes // 1024


def main() -> None:
    while True:
        try:
            bytes = int(input('Введите размер файла (в байтах): '))
        except ValueError as e:
            print(f'{e} Попробуйте снова...')
        else:
            kilobytes = convert_bytes_to_kilobytes(bytes)
            print(f'Размер файла в килобайтах = {kilobytes}')


if __name__ == '__main__':
    main()