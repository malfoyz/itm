A, B = map(int, input('Введите числа A и B через пробел: ').split())
print(A % 2 == 1 and B % 2 == 0 or A % 2 == 0 and B % 2 == 1)