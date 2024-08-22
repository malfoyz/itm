"""
Менеджеры позволяют передавать целые объекты между процессами.
Менджеры позволяют использовать общую память, создавать нужные нам структуры,
и передавать эти структуры между разными процессами.

Отличие от Array в том, что мы можем передавать не только массивы.
"""

import multiprocessing
import time
import random

from multiprocessing import Process, Manager


def f(m_dict, m_array):
    m_dict['name'] = 'test'
    m_dict['version'] = '1.0'
    m_array.append(1)
    m_array.append(2)



def main():
    with Manager() as m:
        d = m.dict()
        l = m.list()
        pr = Process(target=f, args=(d,l,))
        pr.start()
        pr.join()

        print('dict:', d)
        print('list:', l)


if __name__ == '__main__':
    main()
