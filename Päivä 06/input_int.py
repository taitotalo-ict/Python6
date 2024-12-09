def input_int(question: str='') -> int|None:
    """Asks user using the question and accepts only an integer number as answer.
    Returns the integer version of the answer"""
    while True:
        try:
            return int(input(question))
        except ValueError:
            print('Vain numeroa!')



try:
    numero = input_int('Numero? ')
except KeyboardInterrupt:
    pass