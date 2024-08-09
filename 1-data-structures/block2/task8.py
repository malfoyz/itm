def reverse_number(number: int) -> int:
    if number < 10 or number > 99:
        raise ValueError('Число должно быть двузначным!')
    left, right = number // 10, number % 10
    return right * 10 + left


def main() -> None:
    while True:
        try:
            number = int(input('Введите двузначное число: '))
            reversed_number = reverse_number(number)
        except ValueError as e:
            print(f'{e} Попробуйте снова...')
        else:
            print(f'Перевернутое число = {reversed_number}')


if __name__ == '__main__':
    main()