"""
В обычном варианте, пока все потоки не завершатся, главный поток также не завершится.
Чтобы это исправить, нужно сделать поток демоном. И тогда, если завершится поток-демон,
фоновые также завершатся, даже если не успели выполниться до конца.

Если основной поток завершается, демоны-поток также завершаются.
"""

import time
import threading


def get_data(data):
    for _ in range(5):
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(1)


def main():
    thr = threading.Thread(target=get_data, args=(str(time.time()),), daemon=True)
    # или thr.daemon = True
    thr.start()
    print('finish')


if __name__ == '__main__':
    main()