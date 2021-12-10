#!python3

with open('input.txt') as file:
    entries = [
        [
            half.split(' ')
            for half in line.strip().split(' | ')
        ]
        for line in file.readlines()
    ]

count = 0

for entry in entries:
    output = entry[1]
    count += len([
        digit for digit in output
        if len(digit) == 2
        or len(digit) == 3
        or len(digit) == 4
        or len(digit) == 7
    ])

print(f'Result: {count}')
