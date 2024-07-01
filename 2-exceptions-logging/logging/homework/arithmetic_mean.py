"""
Этот модуль содержит функцию для нахождения среднего
арифметического списка чисел.
"""

import logging

from typing import List, Union


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler(f'{__name__}.log', mode='w')
formatter = logging.Formatter('%(name)s %(asctime)s %(levelname)s %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info(f'Тестирование пользовательского логгера для модуля {__name__}')


def arithmetic_mean(numbers: List[Union[int, float]]) -> float:
    """
    Вычисляет среднее арифметическое списка чисел.

    :param numbers: список чисел
    :type numbers: List[Union[int, float]]

    :rtype: float
    :return: среднее арифметическое списка чисел
    """

    logger.info('Пытаемся вычислить среднее арифметическое...')
    try:
        result = sum(numbers) / len(numbers)
        logger.info(f'Результат: {result}')
    except Exception as e:
        print(e)
        logger.error(f'Ошибка: {e}')
    return result