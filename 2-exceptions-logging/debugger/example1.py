from debugger.for_debug import another_func


def my_func(a, b, c):
    print('Хочу поделить')
    c *= 100
    another_func()
    print(c)
    a *= c
    return a / b


print('abc')
d = 3
print(my_func(1, 1, 1))
m = 4
l = [1, 2, 3 ,4 , 5]