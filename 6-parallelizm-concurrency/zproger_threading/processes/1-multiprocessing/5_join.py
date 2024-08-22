import time
import multiprocessing


def test():
    for _ in range(3):
        print(f'{multiprocessing.current_process().name} - {time.time()}')
        time.sleep(5)


prc = []


def main():
    for _ in range(3):
        pr = multiprocessing.Process(target=test)
        prc.append(pr)
        pr.start()

    for i in prc:
        i.join()

    print('Все процессы завершены!')


if __name__ == '__main__':
    main()