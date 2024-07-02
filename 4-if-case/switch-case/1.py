"""
Этот модуль содержит функцию, которая переводит числовую оценку
в описание, а также пример использования данной функции.
"""


def assessment_description(assessment: int) -> str:
    """
    Переводит оценку из целого числа в описательную и возвращает ее.

    :param assessment: числовая оценка
    :type assessment: int

    :rtype: str
    :return: описание оценки
    """
    match assessment:
        case 1:
            description = 'Плохо!'
        case 2:
            description = 'Неудовлетворительно!'
        case 3:
            description = 'Удовлетворительно!'
        case 4:
            description = 'Хорошо!'
        case 5:
            description = 'Отлично!'
        case _:
            description = 'Ошибка!'
    return description


def main() -> None:
    """
    Главная функция, которая запрашивает оценку у пользователя в виде
    числа и выводит описание данной оценки.

    :rtype: None
    :return: None
    """
    while True:
        try:
            assessment = int(input("Введите оценку от 1 до 5: "))
        except Exception as e:
            print(f'{e}. Попробуйте еще раз...')
        else:
            description = assessment_description(assessment)
            print(description)


if __name__ == '__main__':
    main()