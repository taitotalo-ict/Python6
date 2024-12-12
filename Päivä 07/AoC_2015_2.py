
file = open(r'S:\Christian Finnberg\Ohjelmointi\Python\AoC\2015\input_2015_2.txt', 'r')
#input_lista = tuple(map(str.rstrip, file.readlines()))

# input_lista: list[str] = []
# for line in file.readline():
#     input_lista.append(line.rstrip())

input_lista = file.read().rstrip().split()


paper = 0
ribbon = 0
for line in input_lista:
    l, w, h = map(int, line.split('x'))
    paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    ribbon += min(2*l+2*w, 2*w+2*h, 2*l+2*h) + (l*w*h)

print('Part 1:', paper)
print('Part 2:', ribbon)