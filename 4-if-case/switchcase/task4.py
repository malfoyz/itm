"""
Этот модуль содержит функцию, выполняющую команду и возвращающую
конечное направление робота, а также пример использования
данной функции.
"""


def execute_command(initial_direction: str, command: int) -> str:
    """
    Выполняет команду движения робота.

    :param initial_direction: начальное направление робота
    :type initial_direction: str
    :param command: команда движения робота
    :type command: int

    :rtype: str
    :return: конечное направление робота после выполнения команды
    """
    direction = initial_direction
    match initial_direction:
        case 'С':
            match command:
                case 1:
                    direction = 'В'
                case -1:
                    direction = 'З'
        case 'Ю':
            match command:
                case 1:
                    direction = 'З'
                case -1:
                    direction = 'В'
        case 'З':
            match command:
                case 1:
                    direction = 'С'
                case -1:
                    direction = 'Ю'
        case 'В':
            match command:
                case 1:
                    direction = 'Ю'
                case -1:
                    direction = 'С'
        case _:
            print('Нет такого направления!')

    return direction


def main() -> None:
    """
    Главная функция, которая запрашивает у пользователя текущее направление
    робота, команду движения робота и выводит конечное направление робота.

    :rtype: None
    :return: None
    """
    while True:
        try:
            direction = input('Введите исходное направление робота ("C", "Ю", "З", "В"): ')
            print('Введите одну из команд:',
                  '0 : продолжать движение',
                  '1 : поворот налево',
                  '-1 : поворот направо',
                  sep='\n')
            command = int(input())
        except Exception as e:
            print(f'{e}. Попробуйте еще раз...')
        else:
            print('Текущее направление: ', execute_command(direction, command))


if __name__ == '__main__':
    main()