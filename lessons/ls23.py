from __future__ import annotations

class Point: 
    x: float
    y: float

    def __init__(self, x: float, y:float):
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x,y)
    
    def __add__(self, other: Point) -> Point:
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x,y)

a: Point = Point(1.0, 2.0)
b: Point = Point(3.0, 4.0)
# c: Point = a.add(b)
# print(f"Poinr C {c.x}, {c.y}")
d: Point = a + b
print(f"Point D: {d.x}, {d.y}")



