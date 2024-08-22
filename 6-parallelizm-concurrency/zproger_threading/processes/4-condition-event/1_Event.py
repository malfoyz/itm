"""
Технологии синхронизации Condition и Event позволяют использовать
сигналы и передавать их между разными процессами.

Condition позволяет использовать состояние. Используя его, можно установить выполнение
нужного нам процесса в определенном месте. Его выполнение не продолжится, пока любой из процессов
не сообщит ему об этом.

В отличие от Event, он может отправлять уведомления либо всем процессам сразу, либо определенному процессу.

Event работает по похожему принципу, только у него есть одно базовое состояние:
- либо значение по умолчанию - False - заставляет процесс ждать;
- либо - True - говорит о том, что необходимо начать выполнение.
"""
import multiprocessing
import random
import time

from multiprocessing import Process, Event


def test(event):
    print(multiprocessing.current_process().name)
    print('функция test запущена!')
    while True:
        event.wait()   # ждем, если False, пока не появится True (по умолчанию будет False)
        print('test')
        time.sleep(1)


def test_event(event):
    print(multiprocessing.current_process().name)
    while True:
        time.sleep(5)
        event.set()     # устанавливает Event в True (делаем выполнение)
        print('Event True')
        time.sleep(5)
        event.clear()   # устанавливает Event в False (ждем)
        print('Event False')


def main():
    event = Event()
    Process(target=test, args=(event,)).start()
    Process(target=test_event, args=(event,)).start()


if __name__ == '__main__':
    main()



