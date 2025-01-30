from enum import Enum, auto

class Colors(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()
    WHITE = auto()
    BLACK = auto()

    def is_primary(self):
        return self in (Colors.RED, Colors.GREEN, Colors.BLUE)

print(Colors.RED)
print(Colors.RED.is_primary())      # True
print(Colors.YELLOW.is_primary())   # False
#print(color.is_primary())       

# class Roles(Enum):
#     TEACHER = 1
#     STUDENT = 2
#     ADMIN = 3

# role = Roles.TEACHER

# if (role == Roles.TEACHER):
#     ...

