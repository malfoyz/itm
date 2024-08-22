import os

import pytest


from homework.creating_files import create_file, create_n_files_with_index_inside


@pytest.fixture
def clearing_files():
    """Удаление созданных файлов после тестов"""
    yield
    for i in range(1, 11):
        try:
            os.remove(f'file_{i}.txt')
        except FileNotFoundError:
            pass


def test_create_n_files_with_index_inside(clearing_files):
    files_count = 10
    create_n_files_with_index_inside(files_count)

    for i in range(1, files_count + 1):
        filename = f'file_{i}.txt'
        assert os.path.exists(filename), f'Filename {filename} does not exist.'

        with open(filename, 'r') as file:
            content = file.read().strip()
            assert content == str(i), f'File {filename} has incorrect content.'