class CustomClassIter:
    def __init__(self, iterable_data) -> None:
        self.iterable_data = iterable_data.copy()
        self.index = 0

    def __next__(self):
        if self.index < len(self.iterable_data):
            value = self.iterable_data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

class CustomClass:
    def __init__(self, data: list) -> None:
        self._data = data
    
    def __iter__(self):
        # return self._data.__iter__()
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self._data):
            value = self._data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

custom_object = CustomClass([1,2,3,4,5])
for val in custom_object:
    print(val)

iterator = custom_object.__iter__()
iterator.__next__() # 1
iterator.__next__() # 2
iterator.__next__() # 3
iterator.__next__() # 4
iterator.__next__() # 5
try:
    iterator.__next__() # StopIteration
except StopIteration:
    print('StopIteration')

iterator = iter(custom_object)
next(iterator) # 1
next(iterator) # 2
next(iterator) # 3
next(iterator) # 4
next(iterator) # 5
#next(iterator) # StopIteration
