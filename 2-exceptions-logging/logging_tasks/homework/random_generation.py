"""
Этот модуль содержит функцию генерации случайных чисел в заданном диапазоне.
"""

import logging
import random

from typing import List


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler(f'{__name__}.log', mode='w')
formatter = logging.Formatter('%(name)s %(asctime)s %(levelname)s %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info(f'Тестирование пользовательского логгера для модуля {__name__}')


def random_generation(min: int, max: int, count:int=1) -> List[int]:
    """
    Вычисляет и возвращает список случайных чисел в заданном диапазоне.

    :param min: левая граница диапазаона возможных чисел
    :type min: int
    :param max: правая граница диапазона возможных чисел
    :type max: int
    :param count: количество чисел, которые необходимо сгенерировать
    :type count: int, default 1

    :rtype: List[int]
    :return: список, состоящий из случайных чисел
    """
    if min < 0:
        logger.error(f'Левая граница диапазона не может быть меньше нуля (min = {min})')
        raise Exception('Левая граница диапазона не может быть меньше нуля.')
    if count < 1:
        logger.error(f'Число элементов должно быть больше 1 (count = {count})')
        raise Exception('Число элементов должно быть больше 1.')

    result = [random.randint(min, max) for i in range(count)]
    logger.info(f'Успех! Список: {result}')
    return result