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
class hexagon:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("My area is :", (3 * (3**0.5) * self.side**2) / 2)
class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("My area is :", 3.14 * self.radius**2)
class pentagon:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("My area is :", (5 * self.side**2) / (4 * (3**0.5)))
class octagon:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("My area is :", 2 * (1 + (2**0.5)) * self.side**2)
class triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        print("My area is :", (self.base * self.height) / 2)
class rhombus:
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
    def area(self):
        print("My area is :", (self.diagonal1 * self.diagonal2) / 2)
class parallelogram:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        print("My area is :", self.base * self.height)
class trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height
    def area(self):
        print("My area is :", ((self.base1 + self.base2) / 2) * self.height)
class nonagon:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("My area is :", (9 * self.side**2) / (4 * (3**0.5)))
class decagon:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("My area is :", (10 * self.side**2) / (4 * (3.14**0.5)))
class dodecagon:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("My area is :", (12 * self.side**2) / (4 * (3.14**0.5)))
class icosagon:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("My area is :", (20 * self.side**2) / (4 * (3.14**0.5)))
osquare = square(5)
orectangle = rectangle(5, 3)
ohexagon = hexagon(5)
ocircle = circle(5)
opentagon = pentagon(5)
ooctagon = octagon(5)
ononagon = nonagon(5)
odecagon = decagon(5)
ododecagon = dodecagon(5)
oicosagon = icosagon(5)
for shape in (osquare, orectangle, ohexagon, ocircle, opentagon, ooctagon, ononagon, odecagon, ododecagon, oicosagon):
    shape.area()
print("This is all I can do for now, but I will learn more shapes in the future")