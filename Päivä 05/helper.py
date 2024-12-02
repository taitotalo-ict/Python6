"""Custom helper functions to be used in different situations"""

def _is_number(string: str) -> bool:
    """Checks that string is composed only with number chars"""
    for char in string:
        if char not in '0123456789':
            return False
    return True

def input_int(question: str='') -> int:
    """Asks user using the question and accepts only 
    an integer number as answer.
    Returns the integer version of the answer"""
    while True:
        answer = input(question)
        if not answer:
            continue
        if _is_number(answer):
            return int(answer)
