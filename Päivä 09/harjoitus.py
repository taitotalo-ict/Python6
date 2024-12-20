from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

with open(SCRIPT_DIR / 'input_2015_3.txt', 'r') as file_handler:
    content = file_handler.read().strip()

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
    house += DIRECTIONS[character]
    # match character:
    #     case '^':
    #         house += 1j
    #     case 'v':
    #         house += -1j
    #     case '<':
    #         house += -1
    #     case '>':
    #         house += 1
    if house not in houses:
        houses.append(house)




print(len(houses))