def _is_number(string):
    for char in string:
        if char not in '0123456789':
            return False
    return True

def input_int(question):
    while True:
        answer = input(question)
        if not answer:
            continue
        if _is_number(answer):
            return int(answer)




