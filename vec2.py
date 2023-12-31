from math import sqrt

class Vec2:
    """Class representing a 2D vector"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):
        """In-place addition (+=)"""
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)
    
    def __isub__(self, other):
        """In-place subtraction (-=)"""
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return Vec2(other * self.x, other * self.y)
    
    __rmul__ = __mul__

    def __truediv__(self, other):
        return Vec2(self.x / other, self.y / other)
    
    def __abs__(self):
        """Return the magnitude of the vector"""
        return sqrt(pow(self.x, 2) + pow(self.y, 2))
    