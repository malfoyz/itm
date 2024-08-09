"""
Этот модуль содержит функцию, переводящую трехзначное число в строку-описание,
а также пример использования данной функции.
"""


def number_description(number: int) -> str:
    """
    Переводит трехзначное число в строку-описание и возвращает ее.

    :param number: трехзначное число
    :type number: int

    :rtype: str
    :return: строка-описание числа
    """
    if number < 100 or number > 999:
        raise Exception('Число должно быть трехзначным!')

    try:
        first_digit, second_digit, third_digit = map(
            int,
            list(str(number))
        )
    except Exception as e:
        print(f'{e}')

    match first_digit:
        case 1:
            result = 'сто '
        case 2:
            result = 'двести '
        case 3:
            result = 'триста '
        case 4:
            result = 'четыреста '
        case 5:
            result = 'пятьсот '
        case 6:
            result = 'шестьсот '
        case 7:
            result = 'семьсот '
        case 8:
            result = 'восемьсот '
        case 9:
            result = 'девятьсот '

    match second_digit:
        case 1:
            result += 'десять '
        case 2:
            result += 'двадцать '
        case 3:
            result += 'тридцать '
        case 4:
            result += 'сорок '
        case 5:
            result += 'пятьдесят '
        case 6:
            result += 'шестьдесят '
        case 7:
            result += 'семьдесят '
        case 8:
            result += 'восемьдесят '
        case 9:
            result += 'девяносто '

    match third_digit:
        case 1:
            result += 'один'
        case 2:
            result += 'два'
        case 3:
            result += 'три'
        case 4:
            result += 'четыре'
        case 5:
            result += 'пять'
        case 6:
            result += 'шесть'
        case 7:
            result += 'семь'
        case 8:
            result += 'восемь'
        case 9:
            result += 'девять'

    return result


def main() -> None:
    """
    Главная функция, которая запрашивает у пользователя трехзначное число,
    переводит его в строку-описание и выводит.

    :rtype: None
    :return: None
    """
    while True:
        try:
            number = int(input('Введите целое трехзначное число: '))
        except Exception as e:
            print(f'{e}. Попробуйте еще раз...')
        else:
            print(number_description(number))


if __name__ == '__main__':
    main()