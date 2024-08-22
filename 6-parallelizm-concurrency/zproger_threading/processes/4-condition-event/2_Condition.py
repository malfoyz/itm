"""
Condition отличается тем, что вызов метода разблокировки
срабатывает только 1 раз.

Так же, когда мы вызываем метод, который переводит Condition в True,
он переводит только на 1 раз. Затем wait() сбрасывается опять в False.
И чтобы опять сработала область после wait() во 2 раз, нужно опять вызвать метод разблокировки.
"""

import time
import random

from multiprocessing import Process, Condition


def f1(cond):
    while True:
        with cond:
            cond.wait()
            print('Получили событие')


def f2(cond):
    for i in range(100):
        if i % 10 == 0:
            with cond:
                cond.notify()  # разблокируем - переводим в True
        else:
            print(f'f2: {i}')
        time.sleep(1)


def main():
    cond = Condition()
    Process(target=f1, args=(cond,)).start()
    Process(target=f2, args=(cond,)).start()


if __name__ == '__main__':
    main()