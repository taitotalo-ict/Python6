from pathlib import Path

BASEDIR = Path(__file__).parent

with open(BASEDIR / 'input_2024_2.txt', 'r') as file:
    # data = []
    # for line in file.readlines():
    #     data.append(line.strip())

    data = [tuple(map(int, line.rstrip().split())) for line in file.readlines()]

# def check_increasing(line: tuple[int, ...]) -> bool:
#     for index in range(1, len(line)):
#         # if not (line[index] > line[index-1]): 
#         if line[index] <= line[index-1]: 
#             return False
#     return True

# def check_increasing(line: tuple[int, ...]) -> bool:
#     pairs = [(line[index-1], line[index]) for index in range(1, len(line))]
#     return all(map(lambda pair: pair[1] > pair[0], pairs))

# def check_decreasing(line: tuple[int, ...]) -> bool:
#     for index in range(1, len(line)):
#         if line[index] >= line[index-1]:
#             return False
#     return True

# def check_decreasing(line: tuple[int, ...]) -> bool:
#     pairs = [(line[index-1], line[index]) for index in range(1, len(line))]
#     return all(map(lambda pair: pair[1] < pair[0], pairs))

# def check_diff(line: tuple[int, ...]) -> bool:
#     for index in range(1, len(line)):
#         if abs(line[index] - line[index-1]) > 3:
#             return False
#     return True

# def check_diff(line: tuple[int, ...]) -> bool:
#     pairs = [(line[index-1], line[index]) for index in range(1, len(line))]
#     return all(map(lambda pair: abs(pair[1] - pair[0]) <= 3, pairs))

# def is_safe(line: tuple[int, ...]) -> bool:
#     pairs = [(line[index-1], line[index]) for index in range(1, len(line))]
#     a = all(map(lambda pair: pair[1] > pair[0], pairs))
#     b = all(map(lambda pair: pair[1] < pair[0], pairs))
#     c = all(map(lambda pair: abs(pair[1] - pair[0]) <= 3, pairs))
#     return (a or b) and c
        
# def is_safe(line: tuple[int, ...]) -> bool:
#     diff = [(line[index] - line[index-1]) for index in range(1, len(line))]
#     a = all(map(lambda d: d > 0, diff))
#     b = all(map(lambda d: d < 0, diff))
#     c = all(map(lambda d: abs(d) <= 3, diff))
#     return (a or b) and c

def is_safe(line: tuple[int, ...]) -> bool:
    diff = [(line[index] - line[index-1]) for index in range(1, len(line))]
    return all(map(lambda d: 1 <= d <= 3, diff)) or \
           all(map(lambda d: -1 >= d >= -3, diff))

# count = 0
# for line in data:
#     safe = False
#     if check_increasing(line) or check_decreasing(line):
#         safe = check_diff(line)
#     if safe:
#         count += 1

# count = 0
# for line in data:
#     if is_safe(line):
#         count += 1

print('Part 1:', sum(is_safe(line) for line in data))

# def is_safe_removing(line: tuple[int, ...]) -> bool:
#     for index in range(len(line)):
#         if is_safe(line[:index] + line[index+1:]):
#             return True
#     return False

def is_safe_removing(line: tuple[int, ...]) -> bool:
    return any(is_safe(line[:index] + line[index+1:]) for index in range(len(line)))

print('Part 2:', sum(is_safe_removing(line) for line in data))