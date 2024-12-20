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

print(len(houses))