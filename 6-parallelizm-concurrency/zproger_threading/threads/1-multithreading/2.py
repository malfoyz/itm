"""
В данном примере поток, работающий с функцией get_data работает в фоновом режиме, благодаря чему
главный поток также работает.
"""

import time
import threading


def get_data(data):
    while True:
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(1)


def main():
    thr = threading.Thread(target=get_data, args=(str(time.time()),), name='thr-1')
    thr.start()

    for i in range(100):
        print(f'current: {i}')
        time.sleep(1)

        if i % 10 == 0:
            print('active thread:', threading.active_count())
            print('enumerate:', threading.enumerate())
            print('thr-1 is alive:', thr.is_alive())


if __name__ == '__main__':
    main()