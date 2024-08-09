class ReadIntX:
    """
    Дискриптор не данных.
    Имеет приоритет такой же, как и обычные атрибуты.
    """
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer:
    """
    Дескриптор данных для координаты.
    Дескриптор данных имеет приоритет выше, чем обычные атрибуты
    """
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        # print(f'__set__: {self.name} = {value}')
        self.verify_coord(value)
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()  # дескриптор НЕ данных

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
print(p.__dict__)
print(p.z)          # 3

print(p.xr)         # 1
p.xr = 5            # создастся локальный атрибут, т.к. дескриптор не данных только для чтения
print(p.xr, p.__dict__)


