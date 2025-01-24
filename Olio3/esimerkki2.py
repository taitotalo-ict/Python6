class Person:
    def __init__(self, first_name:str, last_name:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.first_name}, {self.last_name})'
    
class Teacher(Person):
    def __init__(self, first_name: str, last_name: str) -> None:
        super().__init__(first_name, last_name)
        self.email = f'{first_name.lower()}.{last_name.lower()}@taitotalo.fi'

    # def __repr__(self) -> str:
    #     return f'Teacher({self.first_name}, {self.last_name})'

class Student(Person):
    _count = 0
    def __init__(self, first_name: str, last_name: str) -> None:
        super().__init__(first_name, last_name)
        self.student_id = Student._count
        Student._count += 1
        self.email = f'{first_name[0].lower()}{last_name[0].lower()}{self.student_id:06}@edu.taitotalo.fi'

    def __str__(self) -> str:
        return f'<{self.__class__.__name__}({self.first_name}, {self.last_name})> (ID: {self.student_id})'

p1 = Person('Christian', 'Finnberg')
print(p1)
t1 = Teacher('Matti', 'Suomalainen')
print(t1, t1.email)
s1 = Student('Teijo', 'Tehokas')
s2 = Student('Maija', 'Fiksu')
print(s1, s1.email)
print(s2, s2.email)
print(Student._count)