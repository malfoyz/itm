class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):   # отладочная инфа
        return f'{self.__class__}: {self.name}'

    def __str__(self):    # для пользователя, выводится в print() и str()
        return f'{self.name}'



cat = Cat('Васька')
print(cat)