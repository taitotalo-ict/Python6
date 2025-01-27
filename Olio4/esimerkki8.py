class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, value) -> None:
        self.value = value

obj1 = Singleton(10) 
obj2 = Singleton(20)

print(obj1.value) # 20
print(obj2.value) # 20
print(obj1 is obj2) # True