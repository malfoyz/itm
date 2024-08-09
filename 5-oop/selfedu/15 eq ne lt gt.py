class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целым числом')
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Операнд справа должен быть тип int или Clock')

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc


c1 = Clock(1000)
c2 = Clock(2000)

print(c1 == c2)
print(c1 == 1000)
print(c1 != 1000)
print(c1 < c2)
print(c1 > c2)
print(c1 <= c2)