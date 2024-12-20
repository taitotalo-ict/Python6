number = '3113322113'

for _ in range(40):
    count = 0
    new_number = ''
    previous_char = number[0]
    for char in number:
        if char == previous_char:
            count += 1
        else:
            new_number += str(count) + previous_char
            count = 1
            previous_char = char
    else:
        new_number += str(count) + previous_char

    number = new_number

print('Part 1 (strings):', len(new_number))

# Part 2 (merkkijonoilla) kestää TOSI TOSI kauan

#####

number = list('3113322113')

for _ in range(40):
    count = 0
    new_number = []
    for index in range(len(number)):
        count += 1
        if (index == len(number) - 1) or (number[index] != number[index+1]):
            new_number.append(str(count))
            new_number.append(number[index])
            count = 0
    number = new_number

print('Part 1 (lists):', len(number))

# Part 2:

number = list('3113322113')

for _ in range(50):
    count = 0
    new_number = []
    for index in range(len(number)):
        count += 1
        if (index == len(number) - 1) or (number[index] != number[index+1]):
            new_number.append(str(count))
            new_number.append(number[index])
            count = 0
    number = new_number


print('Part 2 (lists):', len(number))

####

def look_and_say(number: list[str], rounds: int) -> list[str]:
    new_number: list[str] = []
    for _ in range(rounds):
        count:int = 0
        new_number: list[str] = []
        for index in range(len(number)):
            count += 1
            if (index == len(number) - 1) or (number[index] != number[index+1]):
                new_number.append(str(count))
                new_number.append(number[index])
                count = 0
        number = new_number
    return number

number = list('3113322113')
number = look_and_say(list('3113322113'), 40)
print('Part 1 (lists+function):', len(number))
number = look_and_say(number, 10)
print('Part 2 (lists+function):', len(number))
