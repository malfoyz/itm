"""
Происходит хаос, иногда значения повторяются, иногда выводятся в одну строку и т.д.
"""

import time
import threading


value = 0


def inc_value():
    global value
    while True:
        value += 1
        time.sleep(1)
        print(value)


def main():
    for _ in range(5):
        threading.Thread(target=inc_value).start()


if __name__ == '__main__':
    main()