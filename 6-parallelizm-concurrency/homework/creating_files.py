"""
Напишите скрипт, который создаст параллельно 10 файлов
с именем `file_ {index}.txt' и записывает их номер внутрь файла.
"""

import threading


def create_file(index: int) -> None:
    """
    Создает файл и записает туда index.

    :param index: номер файла
    :type index: int

    :return: None
    :rtype: None
    """
    filename = f'file_{index}.txt'
    with open(filename, 'w') as file:
        file.write(str(index))


def create_n_files_with_index_inside(n: int) -> None:
    """
    Создает n файлов, используя многопоточность.

    :param n: количество создаваемых файлов
    :type n: int

    :return: None
    :rtype: None
    """
    for i in range(1, n + 1):
        threading.Thread(target=create_file, args=(i,), name=f'thr_{i}').start()


def main() -> None:
    create_n_files_with_index_inside(10)


if __name__ == '__main__':
    main()