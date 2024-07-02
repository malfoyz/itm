"""
Этот модуль содержит функции вывода всех элементов списка и словаря,
а также пример их использования.
"""

from typing import Any, Dict, List


def iterate_list(lst: List[Any]) -> None:
    """
    Выводит каждый элемент списка на отдельной строке.

    :param lst: список
    :type lst: List[Any]

    :rtype: None
    :return: None
    """
    print('Все элементы списка:')
    for value in lst:
        print(value)


def iterate_dict(dct: Dict[Any, Any]) -> None:
    """
    Выводит каждую пару словаря на отдельной строке.

    :param dct: словарь
    :type dct: Dict[Any, Any]

    :rtype: None
    :return: None
    """
    print('Все элементы словаря:')
    for key, value in dct.items():
        print(key, value)


def main() -> None:
    """
    Главная функция выводящщая все элементы списка и словаря.

    :rtype: None
    :return: None
    """
    iterate_list([1, 6.23, 3, 'cat', 5, True, 10, False])
    iterate_dict({'name': 'Sergey', 'age': 23, 'is_student': True})


if __name__ == '__main__':
    main()