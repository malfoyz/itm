import timeit
import tracemalloc

from block6.task1 import binary_search


def main() -> None:
    arr = list(range(1000000))
    target = 999999

    # профилирование времени
    time = timeit.timeit(lambda: binary_search(arr, target), number=10000)
    print(f"Время выполнения: {time} секунд на 10000 вызовов")

    # профилирование памяти
    tracemalloc.start()
    binary_search(arr, target)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f'Текущая память: {current} байт. Пиковая память: {peak} байт')


if __name__ == '__main__':
    main()