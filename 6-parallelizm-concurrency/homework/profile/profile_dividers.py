import timeit
import tracemalloc

from homework.dividers import get_dividers_with_mulptiprocessing


def main() -> None:
    number = 20000000

    # профилирование времени
    time = timeit.timeit(lambda: get_dividers_with_mulptiprocessing(number), number=1)

    print(f"Время выполнения: {time} секунд.")

    # профилирование памяти
    tracemalloc.start()
    get_dividers_with_mulptiprocessing(number)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f'Текущая память: {current} байт. Пиковая память: {peak} байт')


if __name__ == '__main__':
    main()