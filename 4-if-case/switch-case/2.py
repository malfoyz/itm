"""
Этот модуль содержит функцию, определяющую число дней в месяце,
а также пример использования данной функции.
"""


def days_in_month_count(month_number: int) -> int:
    """
    Определяет и возвращает число дней в месяце.

    :param month_number: номер месяца (от 1 до 12)
    :type month_number: int

    :rtype: int
    :return: число дней в месяце
    """
    if month_number > 12 or month_number < 1:
        raise Exception('Номер месяца должен быть от 1 до 12!')

    match month_number:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 28



def main() -> None:
    """
    Главная функция, которая запрашивает у пользователя номер месяца
    и выводит число дней в данном месяце.

    :rtype: None
    :return: None
    """
    while True:
        try:
            month_number = int(input('Введите номер месяца: '))
            print('Число дней в данном месяце: ',
                  days_in_month_count(month_number))
        except Exception as e:
            print(f'{e}. Попробуйте еще раз...')


if __name__ == "__main__":
    main()