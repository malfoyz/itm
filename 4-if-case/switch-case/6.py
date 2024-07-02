"""

"""


def main() -> None:
    number1, number2 = map(
        float,
        input('Введите 2 числа через пробел: ').split()
    )
    operation = input('Введите операцию: ')

    match operation:
        case '+':
            print(f'{number1} + {number2} = {number1 + number2}')
        case '-':
            print(f'{number1} - {number2} = {number1 - number2}')
        case '*':
            print(f'{number1} * {number2} = {number1 * number2}')
        case '/':
            try:
                print(f'{number1} / {number2} = {number1 / number2}')
            except ZeroDivisionError:
                print('Второе число равно нулю. Деление на 0 невозможно.')


if __name__ == '__main__':
    main()