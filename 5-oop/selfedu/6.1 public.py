class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


pt = Point(1, 2)
pt.x = 200
pt.y = 'coord_y'
print(pt.x, pt.y)