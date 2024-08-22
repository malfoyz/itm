"""
Использование local() работает только в локальной области данного потока.
"""

import time
import threading

data = threading.local()


def get_name():
    print(data.name)


def t1():
    data.name = threading.current_thread().name
    get_name()

def t2():
    data.name = threading.current_thread().name
    get_name()


def main():
    threading.Thread(target=t1).start()
    threading.Thread(target=t2).start()


if __name__ == '__main__':
    main()