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
        locker.acquire()   # блокируем доступ к данной области для остальных потоков
        value += 1
        print(value)
        time.sleep(0.1)
        locker.release()   # освобождаем доступ к данной области


def main():
    for _ in range(5):
        threading.Thread(target=inc_value).start()


if __name__ == '__main__':
    main()