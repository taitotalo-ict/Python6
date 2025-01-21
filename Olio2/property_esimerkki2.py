class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    @property
    def password(self):
        raise AttributeError('Password is write-only')

    @password.setter
    def password(self, new_password):
        self._hashed_password = hash(new_password)

    def check_password(self, password_to_check):
        return self._hashed_password == hash(password_to_check)

    

christian = User('christian', 'abcd1234')
print(christian._hashed_password)
# print(christian.password)
# christian.check_password('qwerty')      # False
# christian.check_password('abcd1234')    # True
