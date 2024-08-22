"""
Барьер ждет, пока до него дойдет указанное кол-во потоков, и только затем идет его выполнение.
"""

import random
import time
import threading


def test(barrier):
    slp = random.randint(10, 15)
    time.sleep(slp)
    print(f'Поток [{threading.current_thread().name}] запущен в ({time.ctime()})')

    barrier.wait()
    print(f'Поток [{threading.current_thread().name}] преодолел барьер в ({time.ctime()})')



def main():
    bar = threading.Barrier(5)
    for i in range(5):
        threading.Thread(target=test, args=(bar,), name=f'thr-{i}').start()


if __name__ == '__main__':
    main()

