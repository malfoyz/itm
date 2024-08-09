"""
Этот модуль является главным модулем, который тестирует логирование функций
из других модулей.
"""

import logging

from arithmetic_mean import arithmetic_mean
from quadratic_equation import quadratic_equation
from random_generation import random_generation


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler(f'{__name__}.log', mode='w')
formatter = logging.Formatter('%(name)s %(asctime)s %(levelname)s %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info(f'Тестирование пользовательского логгера для модуля {__name__}')


def main() -> None:
    """
    Главная функция, тестирующая функции:
     - вычисления квадратного уравнения
     - генерации случайных чисел
     - вычисления арифметического среднего.

    :rtype: None
    :return: None
    """

    '''
    while True:
        logger.info('Пробуем получить коэф. уравнения от пользователя...')

        try:
            a, b, c = map(float, input('Введите коэф. a, b, c через пробел: ').split())

            logger.info(f'Вызываем функцию quadratic_equation c коэффициенты. a = {a}, b = {b}, c = {c}')
            x = quadratic_equation(a, b, c)
        except ValueError as e:
            logger.error(e)
        except Exception as e:
            print(f'{e} Попробуйте снова ввести корни уравнения.')
            logger.exception('Функция quadratic_equation отработала неверно, в ней вызвано исключение.')
        else:
            print(f'Корни уравнения: {x}')
            logger.info(f'Функция quadratic_equation отработала успешно, корни уравнения = {x}')
    '''

    '''
    while True:
        logger.info('Пробуем получить границы диапазона и число элементов...')

        try:
            min, max = map(int, input("Введите границы диапазона для списка случайных чисел через пробел: ").split())
            count = int(input('Введите число элементов списка: '))

            logger.info(f'Вызываем функцию random_generation')
            numbers = random_generation(min, max, count)
        except ValueError as e:
            logger.exception(e)
        except Exception as e:
            print(f'{e} Попробуйте снова ввести границы и число элементов.')
            logger.error('Функция random_generation отработала неверно, вызвано исключение.')
        else:
            print(f'Список: {numbers}')
            logger.info(f'Функция random_generation отработала успешно, список = {numbers}')
    '''

    while True:
        logger.info('Пробуем получить список чисел...')

        try:
            lst = list(map(float, input('Введите список чисел через пробел: ').split()))

            logger.info(f'Вызываем функцию arithmetic_mean')
            mean = arithmetic_mean(lst)
        except Exception as e:
            print(f'Ошибка: {e}')
            logger.exception(e)
        else:
            print(f'Среднее арифметическое: {mean}')
            logger.info(f'Функция aritmetic_mean отработала успешно, среднее арифметическое = {mean}')


if __name__ == '__main__':
    main()