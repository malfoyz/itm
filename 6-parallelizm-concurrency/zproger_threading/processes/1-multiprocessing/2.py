import time
import multiprocessing


def test():
    while True:
        print(f'{multiprocessing.current_process().name} - {time.time()}')
        time.sleep(1)


def main():
    pr = multiprocessing.Process(target=test, name='prc-1')
    pr.start()

    print('is_alive:', pr.is_alive())
    print('process id:', pr.pid)



if __name__ == '__main__':
    main()