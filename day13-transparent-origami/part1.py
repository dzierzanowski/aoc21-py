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

for inst in instructions[:1]:
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

print(f'Dot count: {len(dots)}')
