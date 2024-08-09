class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property()
    old = old.setter(set_old)
    old = old.getter(get_old)



p = Person('Сергей', 20)
p.old = 35
print(p.old, p.__dict__)

p.__dict__['old'] = 'old in object p'
print(p.__dict__)