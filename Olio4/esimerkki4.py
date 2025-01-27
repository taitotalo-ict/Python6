from multipledispatch import dispatch

class MyClass:
    @dispatch(int, int)
    def process(self, a: int, b: int):
        print(f"Processing integers {a} and {b}")

    @dispatch(str, str)
    def process(self, a: str, b: str):
        print(f"Processing strings: '{a}' and '{b}'")

    @dispatch(bool, list)
    def process(self, a: bool, b: list):
        print(f"Processing bool {a} and list {b}")

my_object = MyClass()
my_object.process(10, 20)  # Processing integers 10 and 20
my_object.process("hello" , "world")  # Processing strings 'hello' and 'world'
my_object.process(True, [1, 2, 3])  # Processing bool True and list [1, 2, 3]