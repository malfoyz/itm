class Point:
    """Класс для представления координат точек на плоскости"""
    color = 'red'
    circle = 2


print(Point.color)
Point.color = 'black'
print(Point.color)

print(f'Все атрибуты класса: {Point.__dict__}')

a = Point()
b = Point()

print(f'Тип: {type(a)}')
print(type(a) == Point)
print(isinstance(a, Point))

print(f'Все атрибуты самого объекта: {a.__dict__}')
a.color = 'green'
print(a.color, b.color)
print(f'Все атрибуты самого объекта: {a.__dict__}')

Point.type_pt = 'disc'
print(Point.type_pt)
print(a.type_pt)

setattr(Point, 'prop', 1)
setattr(Point, 'type_pt', 'square')

# print(Point.a)
print(getattr(Point, 'a', False))

del Point.prop
# del Point.prop Ошибка, т.к. уже его нет

print(hasattr(Point, 'prop'))

delattr(Point, 'type_pt')
# delattr(Point, 'type_pt')

a.x = 1
a.y = 2

b.x, b.y = 3, 4

print(Point.__doc__)
