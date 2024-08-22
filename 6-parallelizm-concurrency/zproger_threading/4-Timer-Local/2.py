"""
"""

import time
import threading


def test():
    while True:
        print('test')
        time.sleep(1)


def main():
    thr = threading.Timer(5, test)
    thr.start()

    for _ in range(3):
        print('111')
        time.sleep(1)

    thr.cancel()    # отменяем таймер
    print('finish')


if __name__ == '__main__':
    main()