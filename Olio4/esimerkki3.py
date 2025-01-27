from functools import singledispatchmethod

class MyClass:
    @singledispatchmethod
    def my_method(self, value):
        print('Oletusmetodi')

    @my_method.register(int)
    def _(self, value):
        print('Int -metodi')

    @my_method.register(str)
    def _(self, value):
        print('Str -metodi')

my_object = MyClass()
my_object.my_method(10)
my_object.my_method('moi')
my_object.my_method([1,2,3])
