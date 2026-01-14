import math
from shapes.point import Point

class Circle:
    def __init__(self, center, radius):
        self.center = center    # center is a Point object
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def display(self):
        print("Center:", self.center.display())
        print("Radius:", self.radius)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())
