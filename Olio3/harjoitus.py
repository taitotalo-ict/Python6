from math import sqrt
from typing import Self

class Point:
    pass

class Vector:
    def __init__(self, x: int|float, y: int|float) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    # def __ne__(self, other: Self) -> bool:
    #     return not(self.__eq__(other))

    def __neg__(self) -> Self:
        return self.__class__(-self.x, -self.y)

    def __add__(self, other: Self) -> Self:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.__class__(self.x + other.x, self.y + other.y)
    
    # def __sub__(self, other: Self) -> 'Vector':
    #     if not isinstance(other, Vector):
    #         return NotImplemented
    #     return Vector(self.x - other.x, self.y - other.y)
    
    def __sub__(self, other: Self) -> Self:
        # return self.__add__(self.__neg__(other))
        return self + (-other)
    
    @property
    def length(self) -> float:
        'Return the lenght of the vector.'
        # return sqrt(self.x**2+self.y**2)
        return (self.x**2+self.y**2)**(1/2)

    def __mul__(self, other: int|float) -> Self:
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__(self.x * other, self.y * other)
        return NotImplemented
    
    def __rmul__(self, other: int|float) -> Self:
        return self.__mul__(other)    

v1 = Vector(2, 3)
v2 = Vector(3, 2)
print(v1 == v2)
print(v2 != v1)
print(v1 + v2)
print(v2 + v1)
print(v1 - v2)
print(v2 - v1)
print(-v1)
print(-v2)
print(v1.length)
print(v2.length)
print(v1 * 3)
print(3 * v1)
print(v2 * 5.5)
print(5.5 * v2)


class MuokattuVector(Vector):
    pass

m1 = MuokattuVector(5,6)
m2 = MuokattuVector(3,4)
print(m1+m2)
print(isinstance(m1, Vector))
print(isinstance(m2, Vector))
print(m1+v1)
print(v1+m1)