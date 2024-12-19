from pathlib import Path

# BASEDIR = Path(__file__).parent

# log_file = BASEDIR / 'harjoitus.log'
# conf_file = BASEDIR / 'harjoitus.conf'

dir = Path('C:/Windows')

length = 0
for item in dir.glob('*'):
    if item.is_file():
        length += item.stat().st_size

print(f'Files in {dir.absolute()} occupy {length/1024/1024} Megabytes.')