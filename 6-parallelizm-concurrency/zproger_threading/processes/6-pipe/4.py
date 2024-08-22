import time

from multiprocessing import Pipe, Process


def send_data(conn):
    conn.send('hello world')
    conn.send('hello world')
    # conn.close()


def main():
    output_c, input_c = Pipe()
    Process(target=send_data, args=(input_c,)).start()
    Process(target=send_data, args=(input_c,)).start()
    print('data:', output_c.recv())
    print('data:', output_c.recv())
    print('data:', output_c.recv())
    print('data:', output_c.recv())



if __name__ == '__main__':
    main()


