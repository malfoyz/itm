"""
Этот модуль содержит функцию вычисления корней квадртного уравнения.
"""

import logging

from typing import Union, Tuple


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler(f'{__name__}.log', mode='w')
formatter = logging.Formatter('%(name)s %(asctime)s %(levelname)s %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info(f'Тестирование пользовательского логгера для модуля {__name__}')

def quadratic_equation(a: float, b: float, c: float) \
        -> Union[Tuple[float], Tuple[float, float]]:
    """
    Вычисляет и возвращает корни квадратного уравнения.

    :param a: коэффициент a
    :type a: float
    :param b: коэффициент b
    :type b: float
    :param c: коэффициент c

    :rtype: Union[Tuple[float], Tuple[float, float]]
    :return: кортеж, содержащий один или два корня квадратного уравнения
    """

    logger.info(f'a = {a}, b = {b}, c = {c}')

    D = b ** 2 - 4 * a * c

    logger.info(f'D = {D}')

    if D < 0:
        logger.error('D < 0, действительных корней нет.')
        raise Exception('D < 0, действительных корней нет.')
    elif D == 0:
        x = (-b / (2 * a),)
        logger.info(f'Так как D == 0, то x = {x}')
    else:
        x = ((-b + D ** 0.5) / (2 * a),
             (-b - D ** 0.5) / (2 * a))
        logger.info(f'Так как D > 0, то x = {x}')
    return x


