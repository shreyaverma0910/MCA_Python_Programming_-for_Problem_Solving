from shapes.circle import Point, Circle

# Create a point for the center
center_point = Point(3, 4)

# Create a circle with the center point
my_circle = Circle(center_point, 5)

print(my_circle.display())
print("Area:", my_circle.area())
print("Perimeter:", my_circle.perimeter())
