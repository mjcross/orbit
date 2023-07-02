from math import sqrt

class Vec2:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vec2(other * self.x, other * self.y)

    def __rmul__(self, other):
        return Vec2(other * self.x, other * self.y)

    def __truediv__(self, other):
        return Vec2(self.x / other, self.y / other)
    
    def __abs__(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))