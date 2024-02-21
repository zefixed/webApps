import math
import numpy as np

class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x: int = x      
        self.y: int = y      
        self.z: int = z      
        
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def _toList(self) -> list[int]:
        return [self.x, self.y, self.z]
        
    def dot(self, a):
        return np.dot(self._toList(), a._toList()) 
        
    def cross(self, a):
        return np.cross(self._toList(), a._toList())   
        
    def absolute(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

def plane_angle(a: Point, b: Point, c: Point, d: Point):
    x = Point(*(b - a).cross(c - b))
    y = Point(*(c - b).cross(d - c))
    print(x.cross(y) / (x.absolute() * y.absolute()))
    

if __name__ == '__main__':
    plane_angle(Point(5, 6, 3), Point(1, 7, 4), Point(2, 6, 9), Point(2, 4, 8))
