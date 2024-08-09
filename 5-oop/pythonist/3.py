class B:
    def x(self):
        print('x: B')


class C:
    def x(self):
        print('x: C')


class D(B, C):
    pass


d = D()
d.x()
print(D.mro())
