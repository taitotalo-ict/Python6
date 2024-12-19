with open(r'S:\Christian Finnberg\Ohjelmointi\Python\AoC\2015\input_2015_2.txt', 'r') as file:
    file_content = file.readlines()

paper = 0
ribbon = 0
for line in file_content:
    l, w, h = map(int, line.rstrip().split('x'))
    paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    ribbon += min(2*l+2*w, 2*w+2*h, 2*l+2*h) + (l*w*h)

print('Part 1:', paper)
print('Part 2:', ribbon)