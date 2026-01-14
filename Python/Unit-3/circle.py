# circle.py

import math

# Point class to represent coordinates
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        return f"({self.x}, {self.y})"


# Circle class
class Circle:
    def __init__(self, center, radius):
        if not isinstance(center, Point):
            raise TypeError("center must be a Point object")
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def display(self):
        return f"Circle with center at {self.center.display()} and radius {self.radius}"
