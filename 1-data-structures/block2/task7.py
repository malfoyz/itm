from typing import Tuple


def calculate_digits_sum_comp(number: int) -> Tuple[int, int]:
    if number < 10 or number > 99:
        raise ValueError('Число должно быть двузначным!')
    left, right = number // 10, number % 10
    summ, comp = left + right, left * right
    return summ, comp


def main() -> None:
    while True:
        try:
            number = int(input('Введите двузначное число: '))
            summ, comp = calculate_digits_sum_comp(number)
        except ValueError as e:
            print(f'{e} Попробуйте снова...')
        else:
            print(f'Сумма цифр = {summ}, произведение цифр = {comp}')


if __name__ == '__main__':
    main()