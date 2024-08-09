class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print('__call__')
        self.__counter += 1
        return self.__counter


c = Counter()
c2 = Counter()
c()
c()
res = c()
res2 = c2()
print(res, res2)