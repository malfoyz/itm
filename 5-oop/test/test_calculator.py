import pytest


from homework.calculator import Calculator, CalculatorConc


class TestCalculator:
    @pytest.mark.parametrize('a, b, expected_result',
                             [(1, 2, 3),
                              (4.2, 5.8, 10),
                              (2, 2.4, 4.4)])
    def test_add_with_correct_data(self, a, b, expected_result):
        calc = Calculator()
        assert calc.add(a, b) == expected_result

    @pytest.mark.parametrize('a, b',
                             [('asas', 12),
                              (4.2, 'DSADA'),
                              ('sds', 'sdas')])
    def test_add_with_uncorrect_data(self, a, b):
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.add(a, b)


class TestCalculatorConc:
    @pytest.mark.parametrize('a, b, expected_result',
                             [(1, 2, '12'),
                              (4.2, 5.8, '4.25.8'),
                              (2, 2.4, '22.4')])
    def test_add_with_correct_data(self, a, b, expected_result):
        calc = CalculatorConc()
        assert calc.add(a, b) == expected_result

    @pytest.mark.parametrize('a, b',
                             [('asas', 12),
                              (4.2, 'DSADA'),
                              ('sds', 'sdas')])
    def test_add_with_uncorrect_data(self, a, b):
        calc = CalculatorConc()
        with pytest.raises(TypeError):
            calc.add(a, b)

    def test_inheritance(self):
        calc = CalculatorConc()
        assert isinstance(calc, Calculator)