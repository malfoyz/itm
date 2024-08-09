"""
Этот модуль содержит класс калькулятора, а также пример его использования.
"""

from typing import Union


class Calculator:
    """Класс калькулятор"""

    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Считает сумму двух чисел"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError('Числа должны быть целыми или вещественными')

        return a + b


class CalculatorConc(Calculator):
    """Класс калькулятора, который складывает числа с помощью конкатенации"""

    def add(self, a: Union[int, float], b: Union[int, float]) -> str:
        """Складывает числа с помощью конкатенации строк и возвращает полученную строку"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError('Числа должны быть целыми или вещественными')

        return str(a) + str(b)


def main() -> None:
    calc = Calculator()
    print(calc.add(1, 4))

    calc2 = CalculatorConc()
    print(calc2.add(1, 4))


if __name__ == '__main__':
    main()