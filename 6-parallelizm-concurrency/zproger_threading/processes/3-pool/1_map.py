"""
С помощью map происходит распределение аргументов из итерируемого элемента
(например, списка) и процессы вызываются с этими аргументами, распределяя нагрузку между собой.
"""

import random
import multiprocessing


def get_value(value):
    name = multiprocessing.current_process().name
    print(f'[{name}] value: {value}')


def main():
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
       p.map(get_value, list(range(100)))


if __name__ == '__main__':
    main()