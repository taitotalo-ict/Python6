class MyClass:
    def my_method(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            return args[0] + 1
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str):
            return args[0] + args[1]
        else:
            raise TypeError('Parameters count and type not supported.')

my_object = MyClass()
print(my_object.my_method(10))
print(my_object.my_method('moi'))
