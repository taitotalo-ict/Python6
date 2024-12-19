with open(r'S:\Christian Finnberg\Ohjelmointi\Python\AoC\2015\input_2015_2.txt', 'r') as file:
    data = [tuple(map(int, line.rstrip().split('x'))) for line in file.readlines()]

# paper = 0
# for l, w, h in data:
#     paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)


# ribbon = 0
# for l, w, h in data:
#     ribbon += min(2*l+2*w, 2*w+2*h, 2*l+2*h) + (l*w*h)

paper = sum(2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l) for l, w, h in data)
ribbon = sum(min(2*l+2*w, 2*w+2*h, 2*l+2*h) + (l*w*h) for l, w, h in data)

print('Part 1:', paper)
print('Part 2:', ribbon)