"""
Pipe (трубы или каналы) позволяют передавать информацию между разными процессами.
Позволяет передавать любую информацию.

Pipe() возвращает 2 значения:
- одно значение для отправки данных - send()
- другое значение для получения данных - recv()
Причем неважно, как первое значение может быть для отправки/получения, так и второе. Порядок неважен.
"""

import time

from multiprocessing import Pipe, Process


def send_data(conn):
    conn.send('hello world')
    conn.close()


def main():
    output_c, input_c = Pipe()
    p = Process(target=send_data, args=(input_c,))
    p.start()
    p.join()
    print('data:', output_c.recv())



if __name__ == '__main__':
    main()


