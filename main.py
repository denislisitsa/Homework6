import math


class Frange:
    def __init__(self, start, stop=None, step=1.0):
        if stop is None:
            start, stop = 0.0, start
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        current = self.start
        if self.step > 0:
            while current < self.stop:
                yield current
                current += self.step
        elif self.step < 0:
            while current > self.stop:
                yield current
                current += self.step
        else:
            raise ValueError("Step cannot be zero.")


assert (list(Frange(5)) == [0, 1, 2, 3, 4])
assert (list(Frange(2, 5)) == [2, 3, 4])
assert (list(Frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(Frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(Frange(1, 5)) == [1, 2, 3, 4])
assert (list(Frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(Frange(0, 0)) == [])
assert (list(Frange(100, 0)) == [])

print('SUCCESS!')


class colorizer:
    def __init__(self, color):
        self.color = color

    def __enter__(self):
        print('\033[' + self.color + 'm', end='')

    def __exit__(self, exc_type, exc_value, traceback):
        print('\033[0m', end='')


print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')

with colorizer('red'):
    print('printed in red')
print('printed in default color')


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def __contains__(self, point):
        distance_squared = (point.x - self.x) ** 2 + (point.y - self.y) ** 2
        return distance_squared <= self.radius ** 2


class Rectangle(Shape):
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
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass


r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)

c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)

p = Parallelogram(1, 2, 20, 30, 45)

scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)

print(scene.total_square())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(1, 2)
print(p1 in c1)
