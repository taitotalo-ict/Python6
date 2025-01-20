
class Employee:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{first_name.lower()}.{last_name.lower()}@taitotalo.fi'

    def get_email(self):
        return self.email

christian = Employee('Christian', 'Finnberg')
print(christian.email)


