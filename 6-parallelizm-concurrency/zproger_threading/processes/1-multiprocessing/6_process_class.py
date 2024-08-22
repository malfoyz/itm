import time
import multiprocessing


class Process(multiprocessing.Process):
    def run(self):
        print('work')


def main():
    pr = Process()
    pr.start()


if __name__ == '__main__':
    main()