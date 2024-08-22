"""
Timer позволяет запускать потоки спустя заданное нами время.
Он не блокирует основной код, выполнение основного кода продолжается,
а спустя время запускается нужный поток.
"""

import time
import threading


def test():
    while True:
        print('test')
        time.sleep(1)


def main():
    threading.Timer(10, test).start()

    while True:
        print('111')
        time.sleep(2)


if __name__ == '__main__':
    main()