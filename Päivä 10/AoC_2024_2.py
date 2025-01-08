from pathlib import Path

BASEDIR = Path(__file__).parent

with open(BASEDIR / 'input_2024_2.txt', 'r') as file:
    # data = []
    # for line in file.readlines():
    #     data.append(line.strip())

    data = [tuple(map(int, line.rstrip().split())) for line in file.readlines()]

def check_increasing(line: tuple[int, ...]) -> bool:
    for index in range(1, len(line)):
        if not (line[index] > line[index-1]):
            return False
    return True

def check_decreasing(line: tuple[int, ...]) -> bool:
    for index in range(1, len(line)):
        if line[index] >= line[index-1]:
            return False
    return True

def check_diff(line: tuple[int, ...]) -> bool:
    for index in range(1, len(line)):
        if abs(line[index] - line[index-1]) > 3:
            return False
    return True

count = 0
for line in data:
    safe = False
    if check_increasing(line) or check_decreasing(line):
        safe = check_diff(line)
    if safe:
        count += 1

print(count)