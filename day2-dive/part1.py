#!python3

with open('input.txt') as file:
    steps = [
        line.strip().split(' ')
        for line in file.readlines()
    ]

depth = 0
length = 0

for command, value in steps:
    value = int(value)
    if command == 'up':
        depth -= value
    if command == 'down':
        depth += value
    if command == 'forward':
        length += value

print(f'Result: {depth * length}')
