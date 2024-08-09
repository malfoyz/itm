from typing import Tuple


def get_last_and_average_digit(number: int) -> Tuple[int, int]:
    if number < 100 or number > 999:
        raise ValueError('Число должно быть трехзначным!')
    last_digit = number % 10
    average_digit = (number // 10) % 10
    return last_digit, average_digit


def main() -> None:
    while True:
        try:
            number = int(input('Введите трехзначное число: '))
            last_digit, average_digit = get_last_and_average_digit(number)
        except ValueError as e:
            print(f'{e} Попробуйте снова...')
        else:
            print(f'Последняя цифра = {last_digit}, Средняя цифра = {average_digit}')


if __name__ == '__main__':
    main()