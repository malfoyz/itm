import time
from threading import Thread, BoundedSemaphore, current_thread


max_connections = 5
pool = BoundedSemaphore(value=max_connections)


def test():
    with pool:
        print(current_thread().name)
        time.sleep(2)


def main():
    for i in range(10):
        Thread(target=test, name=f'thr-{i}').start()


if __name__ == '__main__':
    main()

