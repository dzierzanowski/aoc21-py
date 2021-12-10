#!python3

with open('input.txt') as file:
    steps = [
        line.strip().split(' ')
        for line in file.readlines()
    ]

aim = 0
depth = 0
length = 0

for command, value in steps:
    value = int(value)
    if command == 'up':
        aim -= value
    if command == 'down':
        aim += value
    if command == 'forward':
        length += value
        depth += value * aim

print(f'Result: {depth * length}')
