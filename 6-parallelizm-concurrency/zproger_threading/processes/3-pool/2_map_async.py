"""
map_async позволяет после выполнения всех процессов запустить нужный нам callback,
который вернет ответы всех процессов в response
"""

import random
import multiprocessing


def end_func(response):               # параметр response нужен, т.к. callback по умолчанию возвращает результат выполнения
    print('Задание завершено!')
    print(response)


def get_value(value):
    name = multiprocessing.current_process().name
    print(f'[{name}] value: {value}')
    return value


def main():
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.map_async(get_value, list(range(100)), callback=end_func)
        p.close()   # нужно закрыть
        p.join()    # дожидаемся всех процессов в пуле


if __name__ == '__main__':
    main()