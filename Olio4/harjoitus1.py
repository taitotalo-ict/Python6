class Point:
    def __init__(self, param1, param2=None) -> None:
        if param2 is None and isinstance(param1, tuple) and len(param1) == 2:
            self.__init__(*param1)
        elif isinstance(param1, int) and isinstance(param2, int):
            self._init_with_integers(param1, param2)
        else:
            raise TypeError('Wrong types for Point')

    def _init_with_integers(self, x, y):
        self.x = x
        self.y = y

    # def _init_with_tuple(self, param):
    #     if isinstance(param[0], int) and isinstance(param[1], int):
    #         self._init_with_integers(param[0], param[1])
    #     else:
    #         raise TypeError('Wrong types for Point')

    # def __init__(self, *args):
    #     print(args)


# Vaihtoehtoinen versio '*args' -parametrilla
class Point:
    def __init__(self, *args) -> None:
        if len(args) == 1 and isinstance(args[0], tuple) and len(args[0]) == 2:
            self.__init__(*args[0])
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            self.x = args[0]
            self.y = args[1]
        else:
            raise TypeError('Wrong types for Point')

p1 = Point(4, 5)
print(p1.x) # 4
print(p1.y) # 5
p2 = Point((7, 8))
print(p2.x) # 7
print(p2.y) # 8

p3 = Point(('a', 'b'))
print(p3.x) # a
print(p3.y) # b
# Väärin!