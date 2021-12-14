#!python3

with open('input.txt') as file:
    dots, instructions = file.read().split('\n\n')
    dots = set([
        tuple([
            int(coord) for coord in dot.split(',')
        ])
        for dot in dots.split('\n')
    ])
    instructions = [
        [
            inst for inst in inst.split(' ')[2].split('=')
        ]
        for inst in instructions.split('\n')
    ]

for inst in instructions:
    axis, fold = inst
    fold = int(fold)
    idx = int(axis == 'y')
    dots_to_process = [dot for dot in dots if dot[idx] > fold]
    for dot in dots_to_process:
        dots.remove(dot)
        coord = dot[idx]
        new_dot = list(dot)
        new_dot[idx] = 2 * fold - coord  # Quick maths 😎
        dots.add(tuple(new_dot))

x, y = list(zip(*dots))
max_x = max(x) + 1
max_y = max(y) + 1
sheet = []
for _ in range(0, max_y):
    sheet.append([' '] * max_x )
for x, y in dots:
    sheet[y][x] = "#"

for row in sheet:
        print(''.join(row))
