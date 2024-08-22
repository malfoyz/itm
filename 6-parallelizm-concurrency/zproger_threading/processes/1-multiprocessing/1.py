import time
import multiprocessing


def test():
    while True:
        print(f'{multiprocessing.current_process().name} - {time.time()}')
        time.sleep(1)


def main():
    multiprocessing.Process(target=test, name='prc-1').start()
    multiprocessing.Process(target=test, name='prc-2').start()
    print('Процесс запущен')


if __name__ == '__main__':
    main()