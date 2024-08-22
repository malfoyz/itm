from multiprocessing.managers import BaseManager


def main():
    BaseManager.register('get')
    manager = BaseManager(address=('127.0.0.1', 4444), authkey=b'abc')
    print('client connected')
    manager.connect()

    res = manager.get()
    print('result:', res)


if __name__ == '__main__':
    main()