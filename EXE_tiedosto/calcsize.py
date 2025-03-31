from pathlib import Path
import sys


# print(sys.argv)
if len(sys.argv) > 1:
    folder = Path(sys.argv[1])
else:
    folder = Path('.')
# folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
summa = 0
for item in folder.rglob('*'):
    # print(item, end='')
    if item.is_file():
        # print(f' - Size: {item.stat().st_size}', end='')
        summa += item.stat().st_size
        # print(item.stat().st_size)
    # print()

print(f'\nTotal size: {summa} bytes ({summa/1024/1024:.2f}MB)')
