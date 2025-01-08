from pathlib import Path

BASEDIR = Path(__file__).parent

with open(BASEDIR / 'input_2024_1.txt', 'r') as file:
    column1 = []
    column2 = []
    for line in file.readlines():
        line = line.rstrip()
        num1, num2 = line.split()
        column1.append(int(num1))
        column2.append(int(num2))

column1.sort()
column2.sort()

# column1 = sorted(column1)
# column2 = sorted(column2)

# difference = 0
# for index in range(len(column1)):
#     difference += abs(column1[index] - column2[index])

# difference = 0
# index = 0
# while index < len(column1):
#     difference += abs(column1[index] - column2[index])
#     index += 1


# difference = sum(abs(column1[idx] - column2[idx]) for idx in range(len(column1)))

print('Part 1:', sum(abs(pair[0] - pair[1]) for pair in zip(column1, column2)))

# similarity = 0
# for num in column1:
#     similarity += num * column2.count(num)

similarity = sum(num * column2.count(num) for num in column1)

print('Part 2:', similarity)