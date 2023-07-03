from operator import add, mul
from itertools import repeat

class NumList(list):
    """Subclass of list, with element-wise numeric operations"""

    def __add__(self, other):
        try:
            return map(add, self, other)
        except TypeError:
            # in case `other` is non-iterable
            return map(add, self, repeat(other))

    __radd__ = __add__

    def __mul__(self, other):
        try:
            return map(mul, self, other)
        except TypeError:
            return map(mul, self, repeat(other))

    __rmul__ = __mul__
