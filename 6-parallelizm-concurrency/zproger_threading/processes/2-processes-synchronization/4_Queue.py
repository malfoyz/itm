

import random
import multiprocessing
import time


def get_text(q):
    val = random.randint(0, 10)
    q.put(str(val))


def main():
    queue = multiprocessing.Queue()
    pr_list = []

    for _ in range(10):
        pr = multiprocessing.Process(target=get_text, args=(queue,))
        pr_list.append(pr)
        pr.start()

    for i in pr_list:
        i.join()

    for elem in iter(queue.get, None):
        print(elem)


if __name__ == '__main__':
    main()