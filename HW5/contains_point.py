class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.center_x = x
        self.center_y = y
        self.radius = radius

    def contains(self, p):
        return (p.x - self.center_x) ** 2 + (p.y - self.center_y) ** 2 <= self.radius ** 2


circle = Circle(0, 0, 3)
point = Point(2, 2)
point1 = Point(2, 3)
point2 = Point(-1, 3)
point3 = Point(-1, 1)

print(circle.contains(point))
print(circle.contains(point1))
print(circle.contains(point2))
print(circle.contains(point3))
