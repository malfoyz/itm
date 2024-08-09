def get_first_digit(number: int) -> int:
    if number < 100 or number > 999:
        raise ValueError('Число должно быть трехзначным!')
    return number // 100


def main() -> None:
    while True:
        try:
            number = int(input('Введите трехзначное число: '))
            first_digit = get_first_digit(number)
        except ValueError as e:
            print(f'{e} Попробуйте снова...')
        else:
            print(f'Первая цифра = {first_digit}')


if __name__ == '__main__':
    main()