"""
starmap позволяет передавать несколько аргументов функцию,
которую будут запускать процессы.
"""

import random
import multiprocessing


'''def end_func(response):
    print(response)'''


def out(x, y, z):
    print(f'value: {x} {y} {z}')


def main():
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.starmap(out, [(1, 2, 3), (4, 5, 6)])   # каждый процесс будет брать кортеж из пула и подставлять из него значения в функцию
        p.close()
        p.join()


if __name__ == '__main__':
    main()