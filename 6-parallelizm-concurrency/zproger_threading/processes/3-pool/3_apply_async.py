"""
apply_async вызывает callback для каждой функции отдельно
"""

import random
import multiprocessing


def end_func(response):
    print(response)


def out(x):
    print(f'value: {x}')
    return x


def main():
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        for i in range(10):
            p.apply_async(out, args=(i,), callback=end_func)
        p.close()
        p.join()


if __name__ == '__main__':
    main()