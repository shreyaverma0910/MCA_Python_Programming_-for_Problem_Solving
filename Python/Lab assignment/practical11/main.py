# Absolute imports
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.point import Point

# Create objects
p = Point(0, 0)
c = Circle(p, 5)
r = Rectangle(10, 4)

print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())
