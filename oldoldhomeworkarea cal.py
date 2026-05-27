class square:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("My area is :", self.side**2)
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("My area is :", self.length * self.width)
osquare = square(5)
orectangle = rectangle(5, 3)
for shape in (osquare, orectangle):
    shape.area()