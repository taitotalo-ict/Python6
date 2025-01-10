from pathlib import Path
import re

BASEDIR = Path(__file__).parent

with open(BASEDIR / 'input_2024_3.txt') as file:
    text = file.read()

result = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', text)

# total = 0
# for elem in result:
#     total += int(elem[0])*int(elem[1])

# total = sum(int(elem[0])*int(elem[1]) for elem in result)
total = sum(int(a)*int(b) for a, b in result)

print('Part 1: ', total)