import time
import multiprocessing


def test():
    for _ in range(3):
        print(f'{multiprocessing.current_process().name} - {time.time()}')
        time.sleep(5)


def main():
    pr = multiprocessing.Process(target=test, name='prc-1')
    pr.start()
    pr.join()
    print('Все процессы завершены!')


if __name__ == '__main__':
    main()