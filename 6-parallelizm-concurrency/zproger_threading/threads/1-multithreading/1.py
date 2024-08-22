import time
import threading


def get_data(data):
    while True:
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(1)


def main():
    thr = threading.Thread(target=get_data, args=(str(time.time()),), name='thr-1')
    thr.start()


if __name__ == '__main__':
    main()