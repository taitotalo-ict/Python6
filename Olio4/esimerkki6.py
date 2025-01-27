class MyClass(object):
    def __new__(cls, *args, **kwargs):
        print('Creating instance...')
        print(f'New parameters: {args=} {kwargs=}')
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, value, count):
        print('Initializing instance...')
        self.value = value

obj = MyClass(10, count=20)
print(obj.value)
