
import time
import threading


def get_data(data):
    while True:
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(1)


def main():
    thr = threading.Thread(target=get_data, args=(str(time.time()),), name='thr-1')
    thr.start()

    print('main thread:', threading.main_thread().name)
    threading.main_thread().name = 'result'
    print('main thread:', threading.main_thread().name)


if __name__ == '__main__':
    main()