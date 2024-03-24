import math


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def dot(self, a):
        return self.x * a.x + self.y * a.y + self.z * a.z

    def cross(self, a):
        return Point(self.y * a.z - self.z * a.y,
                     self.z * a.x - self.x * a.z,
                     self.x * a.y - self.y * a.x)

    def absolute(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)


def plane_angle(a: Point, b: Point, c: Point, d: Point):
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    numerator = x.dot(y)
    denominator = x.absolute() * y.absolute()
    angle = math.degrees(math.acos(numerator / denominator))
    return f"{angle:.2f}"


if __name__ == '__main__':
    print(plane_angle(Point(*map(int, input().split())), Point(*map(int, input().split())),
                      Point(*map(int, input().split())), Point(*map(int, input().split()))))
