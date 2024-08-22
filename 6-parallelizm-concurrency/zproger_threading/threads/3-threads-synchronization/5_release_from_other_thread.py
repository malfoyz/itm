"""
Lock может быть разблокирован абсолютно из любого потока, несмотря на то, каким потом он заблокирован.
RLock позволяет разблокировать область только тому потоку, который её заблокировал.
"""

import time
import threading


locker = threading.RLock()   # создаем объект блокировщика


def inc_value():
    print('Блокируем поток...')
    locker.acquire()
    print('Поток разблокирован...')


def main():
    t1 = threading.Thread(target=inc_value)
    t2 = threading.Thread(target=inc_value)
    t1.start()
    t2.start()



if __name__ == '__main__':
    main()