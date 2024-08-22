"""
BaseManager позволяет передавать целые объекты между процессами.
Можно создавать классы, и передавать методы или функции между разными процессами.
Все это реализовывается в виде модели "клиент-сервер".
"""

import time

from multiprocessing.managers import BaseManager


def get_time():
    return time.time()


def main():
    BaseManager.register('get', callable=get_time)
    manager = BaseManager(address=('', 4444), authkey=b'abc')
    server = manager.get_server()
    print('server start')
    server.serve_forever()


if __name__ == '__main__':
    main()


