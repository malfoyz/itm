import random
import time
from threading import Thread, BoundedSemaphore, current_thread


max_connections = 5
pool = BoundedSemaphore(value=max_connections)


def test():
    with pool:
        slp = random.randint(1, 5)
        print(f'{current_thread().name} - sleep ({slp})')
        time.sleep(slp)


def main():
    for i in range(10):
        Thread(target=test, name=f'thr-{i}').start()


if __name__ == '__main__':
    main()

