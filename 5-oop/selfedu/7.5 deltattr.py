class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):  # вызывается при считывании аттрибута через экземпляр класса
        if item == 'x':
            raise ValueError('Доступ запрещен')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):    # вызыывается при установке новых атрибутов, в т.ч. в __init__
        if key == 'z':
            raise AttributeError('Недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)
            # self.x = 10   в таком случае будет рекурсия в этом методе
            # self.__dict__['x'] = value   поэтому лучше делать так

    def __delattr__(self, item):         # вызывается при удалении атрибута из экземпляра класса
        print('__delattr__: ' + item)
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
del pt1.x
print(pt1.__dict__)