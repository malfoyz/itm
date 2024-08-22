import asyncio
import os
import timeit
import tracemalloc

from homework.limited_requests import make_n_limited_get_requests


def main() -> None:
    url = 'http://example.com'
    requests_count = 50
    requests_limit = 10

    # профилирование времени
    time = timeit.timeit(lambda: asyncio.run(make_n_limited_get_requests(url, requests_count, requests_limit)), number=1)

    # профилирование памяти
    tracemalloc.start()
    asyncio.run(make_n_limited_get_requests(url, requests_count, requests_limit))
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f'Текущая память: {current} байт. Пиковая память: {peak} байт')
    print(f"Время выполнения: {time} секунд.")

    filename = f'statuses.txt'
    if os.path.exists(filename):
        os.remove(filename)


if __name__ == '__main__':
    main()