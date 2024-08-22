"""
Метод join позволяет дождаться выполнения нашего потока.
Например, дождаться выполнения 20 потоков, и только потом продолжить выполнение
в главном потоке.
"""

import time
import threading


def get_data(data, value):
    for _ in range(value):
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(1)


def main():
    thr_list = []

    for i in range(3):
        thr = threading.Thread(target=get_data, args=(str(time.time()), i,), name=f'thr-{i}')
        thr_list.append(thr)
        thr.start()

    for i in thr_list:
        i.join()

    print('finish')


if __name__ == '__main__':
    main()