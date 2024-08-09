import timeit
import tracemalloc

from block6.task2 import bubble_sort


def main() -> None:
    arr = list(range(1000,1,-1))

    # профилирование времени
    time = timeit.timeit(lambda: bubble_sort(arr), number=1)
    print(f"Время выполнения: {time} секунд для сортировки из 1000 элементов")

    # профилирование памяти
    tracemalloc.start()
    bubble_sort(arr)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f'Текущая память: {current} байт. Пиковая память: {peak} байт')


if __name__ == '__main__':
    main()