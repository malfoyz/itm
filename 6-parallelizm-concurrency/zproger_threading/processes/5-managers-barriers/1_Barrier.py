"""
Барьер блокирует область памяти, пока до нее не дойдет указанное число процессов.
"""

import multiprocessing
import time
import random

from multiprocessing import Barrier, Process


def f1(bar):
    name = multiprocessing.current_process().name
    sl = random.randint(2, 10)
    print(f'[{name}] - спим {sl} секунд!')
    time.sleep(sl)
    bar.wait()
    print(f'[{name}] - запущено!')


def main():
    b = Barrier(5)  # число процессов, используемых в барьере
    for i in range(10):
        Process(target=f1, args=(b,)).start()


if __name__ == '__main__':
    main()