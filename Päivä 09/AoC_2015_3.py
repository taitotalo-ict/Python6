from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

with open(SCRIPT_DIR / 'input_2015_3.txt', 'r') as file_handler:
    content = file_handler.read().strip()

#
# Part 1
#

x = 0
y = 0
houses = [(x, y)]
for character in content:
    if character == '^':
        y += 1
    elif character == 'v':
        y -= 1
    elif character == '<':
        x -= 1
    elif character == '>':
        x += 1
    if (x, y) not in houses:
        houses.append((x, y))

house = [0, 0]
houses = [house]
for character in content:
    if character == '^':
        house[1] += 1
    elif character == 'v':
        house[1] += -1
    elif character == '<':
        house[0] += -1
    elif character == '>':
        house[0] += 1
    if house not in houses:
        houses.append(house)

house = 0 + 0j  # kompleksiluku
houses = [house]
DIRECTIONS = {'^': 1j, 'v': -1j, '<': -1, '>': 1}
for character in content:
    match character:
        case '^':
            house += 1j
        case 'v':
            house += -1j
        case '<':
            house += -1
        case '>':
            house += 1
    if house not in houses:
        houses.append(house)

house = 0 + 0j  # kompleksiluku
houses = []
DIRECTIONS = {'^': 1j, 'v': -1j, '<': -1, '>': 1}
for character in content:
    house += DIRECTIONS[character]
    if house not in houses:
        houses.append(house)

print('Part 1:', len(houses))

#
# Part 2
#

x_santa = 0
y_santa = 0
x_robot = 0
y_robot = 0
houses = []
for index, character in enumerate(content):
    if index % 2 == 0:
        if character == '^':
            y_santa += 1
        elif character == 'v':
            y_santa -= 1
        elif character == '<':
            x_santa -= 1
        elif character == '>':
            x_santa += 1
        if (x_santa, y_santa) not in houses:
            houses.append((x_santa, y_santa))
    else:
        if character == '^':
            y_robot += 1
        elif character == 'v':
            y_robot -= 1
        elif character == '<':
            x_robot -= 1
        elif character == '>':
            x_robot += 1
        if (x_robot, y_robot) not in houses:
            houses.append((x_robot, y_robot))

x_santa = 0
y_santa = 0
x_robot = 0
y_robot = 0
houses = []
for index in range(0, len(content), 2):
    character_santa = content[index]
    character_robot = content[index+1]
    if character_santa == '^':
        y_santa += 1
    elif character_santa == 'v':
        y_santa -= 1
    elif character_santa == '<':
        x_santa -= 1
    elif character_santa == '>':
        x_santa += 1
    if (x_santa, y_santa) not in houses:
        houses.append((x_santa, y_santa))
    if character_robot == '^':
        y_robot += 1
    elif character_robot == 'v':
        y_robot -= 1
    elif character_robot == '<':
        x_robot -= 1
    elif character_robot == '>':
        x_robot += 1
    if (x_robot, y_robot) not in houses:
        houses.append((x_robot, y_robot))

house_santa = 0 + 0j  # kompleksiluku
house_robot = 0 + 0j  # kompleksiluku
houses = []
DIRECTIONS = {'^': 1j, 'v': -1j, '<': -1, '>': 1}
for index, character in enumerate(content):
    if index % 2 == 0:
        house_santa += DIRECTIONS[character]
        house = house_santa
    else:
        house_robot += DIRECTIONS[character]
        house = house_robot

    if house not in houses:
        houses.append(house)


house = [0 + 0j, 0 + 0j]  # kompleksiluku
houses = []
DIRECTIONS = {'^': 1j, 'v': -1j, '<': -1, '>': 1}
for index, character in enumerate(content):
    house[index % 2] += DIRECTIONS[character]

    if house[index % 2] not in houses:
        houses.append(house[index % 2])

# index = 0
# while index < len(content):
#     ...
#
#     index += 2

print('Part 2:', len(houses))