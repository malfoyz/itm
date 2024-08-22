import os
import timeit
import tracemalloc

from homework.creating_files import create_n_files_with_index_inside


def main() -> None:
    n = 10

    # профилирование времени
    time = timeit.timeit(lambda: create_n_files_with_index_inside(n), number=1)

    print(f"Время выполнения: {time} секунд.")

    # профилирование памяти
    tracemalloc.start()
    create_n_files_with_index_inside(n)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f'Текущая память: {current} байт. Пиковая память: {peak} байт')

    for i in range(n + 1):
        filename = f'file_{i}.txt'
        if os.path.exists(filename):
            os.remove(f'file_{i}.txt')


if __name__ == '__main__':
    main()