# from functools import wraps
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Before')
        print(f'This function is receiving this parameters: {args} and {kwargs}')
        func(*args, **kwargs)
        print('After')
    
    return wrapper

def repeat_decorator(count: int=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return wrapper
    return decorator
                

@repeat_decorator(5)
def test(nimi):
    print('Moi', nimi)

@decorator
def test2(nimi, ikä):
    print(f'{nimi} ja {ikä}')

# test = decorator(func)

test('Christian')
# Before
# Moi
# After

test2('Christian', 50)



# class Test:
#     @property
#     def val(self):
#         return self.value

#     @val.setter
#     def val(self, value):
#         self.value = value

# obj = Test()
# obj.val # 