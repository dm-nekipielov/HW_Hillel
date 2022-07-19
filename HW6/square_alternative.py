import math
from abc import ABC, abstractmethod
from typing import Tuple


class ICoordinates(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class IShape(ABC):
    @abstractmethod
    def square(self):
        pass


class Point(ICoordinates):
    def __init__(self, x, y):
        super().__init__(x, y)


class Circle(IShape, ICoordinates):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def __contains__(self, other):
        return (other.x - self.x) ** 2 + (other.y - self.y) ** 2 <= self.radius ** 2


class Rectangle(IShape, ICoordinates):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):
    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return f'{result}\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def square(self):
        return self.width * self.height * math.sin(self.angle)


class Triangle(IShape, ICoordinates):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def square(self):
        semi_perimeter = (self.x + self.y + self.z) / 2
        return math.sqrt(
            semi_perimeter * (semi_perimeter - self.x) * (semi_perimeter - self.y) * (semi_perimeter - self.z)
        )


class Scene:
    def __init__(self, figures: Tuple[IShape] = ()):
        self._figures = list(figures)

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass


point = Point(2, 2)
point1 = Point(-1, 3)

r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)

c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)

p = Parallelogram(1, 2, 20, 30, 45)
p1 = Parallelogram(1, 2, 20, 30, 45)

t = Triangle(1, 2, 2)

scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)
scene.add_figure(p)
scene.add_figure(p1)
scene.add_figure(t)

print(scene.total_square())
print(point in c)
print(point1 in c1)
