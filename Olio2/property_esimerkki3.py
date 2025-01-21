class Square:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side**2
    
    @property
    def perimeter(self):
        return self.side * 4

box = Square(5)
print(box.area)
print(box.perimeter)

box.side = 3
print(box.area)
print(box.perimeter)

