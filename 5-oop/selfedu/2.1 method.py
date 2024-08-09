class Point:
    color = 'red'
    circle = 2

    def set_coords(self):
        print('Вызов метода set_coords ' + str(self))


pt = Point()
pt.set_coords()

# Point.set_coords()  ошибка, нужен экземпляр
Point.set_coords(pt)