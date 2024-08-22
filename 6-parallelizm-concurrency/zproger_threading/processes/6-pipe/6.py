import time

from multiprocessing import Pipe, Process


def send_data(conn):
    conn.close()
    conn.send('hello world')


def send_data2(conn):
    conn.send('hello 2')


def main():
    output_c, input_c = Pipe()
    Process(target=send_data, args=(input_c,)).start()
    Process(target=send_data2, args=(input_c,)).start()
    print('data:', output_c.recv())



if __name__ == '__main__':
    main()


