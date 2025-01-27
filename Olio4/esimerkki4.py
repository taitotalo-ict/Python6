from multipledispatch import dispatch

@dispatch(int, int)
def process(a: int, b: int):
    print(f"Processing integers {a} and {b}")

@dispatch(str, str)
def process(a: str, b: str):
    print(f"Processing strings: '{a}' and '{b}'")

@dispatch(bool, list)
def process(a: bool, b: list):
    print(f"Processing bool {a} and list {b}")

process(10, 20)  # Processing integers 10 and 20
process("hello" , "world")  # Processing strings 'hello' and 'world'
process(True, [1, 2, 3])  # Processing bool True and list [1, 2, 3]