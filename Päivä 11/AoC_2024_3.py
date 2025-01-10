from pathlib import Path
import re

BASEDIR = Path(__file__).parent

with open(BASEDIR / 'input_2024_3.txt') as file:
#    text = file.read().replace('\n', '')
    text = file.read()

def sum_muls(text: str) -> int:
    result = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', text)
    return sum(int(a)*int(b) for a, b in result)

# total = 0
# for elem in result:
#     total += int(elem[0])*int(elem[1])

# total = sum(int(elem[0])*int(elem[1]) for elem in result)

print('Part 1: ', sum_muls(text))

text2 = re.sub(r"don't\(\).*?(?:do\(\)|$)", '', text, flags=re.DOTALL)
print('Part 2: ', sum_muls(text2))
