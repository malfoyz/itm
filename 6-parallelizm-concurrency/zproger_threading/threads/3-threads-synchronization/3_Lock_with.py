"""
Блокировщик Lock позволяет только одному потоку вмешаться в выделенную область памяти.
"""

import time
import threading


value = 0
locker = threading.Lock()   # создаем объект блокировщика


def inc_value():
    global value
    while True:
        with locker:       # короткая запись используя with
            value += 1
            print(value)
            time.sleep(0.1)


def main():
    for _ in range(5):
        threading.Thread(target=inc_value).start()


if __name__ == '__main__':
    main()