class Student:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self._completed_courses = []
        # self.full_name = f'{self.first_name} {self.last_name}'
    
    def _get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def add_course(self, course):
        self._completed_courses.append(course)

    def print_courses(self):
        if len(self._completed_courses) == 0:
            print(f'Student {self._get_full_name()} has not completed any courses yet')
        else:
            print(f'Student {self._get_full_name()} has completed the following courses:')
            for course in self._completed_courses:
                print(f'- {course}')

christian = Student('Christian', 'Finnberg')
christian.print_courses()
christian.add_course('Python')
christian.add_course('Linux')
christian.print_courses()
print(christian._get_full_name())