"""
В отличие от Lock в потоках: в процессах блокировщик нужно явно передавать аргумент
блокировщика внутрь процесса (функции). В потоках же можно было просто объявить вне процесса (функции)
и могли без аргумента обращаться к нему.
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