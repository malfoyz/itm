"""

"""

import multiprocessing


lock = multiprocessing.Lock()


def get_value(l):
    l.acquire()
    pr_name = multiprocessing.current_process().name
    print(f'Процесс [{pr_name}] запущен')
    # l.release()


def main():
    multiprocessing.Process(target=get_value, args=(lock,)).start()
    multiprocessing.Process(target=get_value, args=(lock,)).start()


if __name__ == '__main__':
    main()