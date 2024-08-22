"""
Так как мы не вызываем функцию release, то ни один поток не сможет продолжить выполнение
"""

import time
import threading


locker = threading.Lock()   # создаем объект блокировщика


def inc_value():
    print('Блокируем поток...')
    locker.acquire()
    print('Поток разблокирован...')


def main():
    for _ in range(5):
        threading.Thread(target=inc_value).start()


if __name__ == '__main__':
    main()