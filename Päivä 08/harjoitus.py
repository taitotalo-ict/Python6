from pathlib import Path

# BASEDIR = Path(__file__).parent

# log_file = BASEDIR / 'harjoitus.log'
# conf_file = BASEDIR / 'harjoitus.conf'


# 
# Laske 'C:\Windows' -kansion **tiedostojen** pituuden yhteensä
#
dir = Path('C:/Windows')

# length = 0
# for item in dir.glob('*'):
#     if item.is_file():
#         length += item.stat().st_size

length = sum(item.stat().st_size for item in dir.glob('*') if item.is_file())

print(f'Files in {dir.absolute()} occupy {length/1024/1024:.2f} Megabytes.')


#
# Löytää ja printaa 'ipython.exe' -tiedoston polku käyttäjän kotikansiosta
#

file_exists = False
for item in Path.home().rglob('*'):
    if item.name == 'ipython.exe':
        print(item.absolute())
        file_exists = True

if not file_exists:
    print("File can't be found")

# files = [item.absolute() for item in Path.home().rglob('*') if item.name == 'ipython.exe']

# for item in files:
#     print(item)





