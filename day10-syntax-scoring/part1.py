#!python3

with open('input.txt') as file:
    lines = file.read().split('\n')

mapping = {
    ')': { 'opening': '(', 'points': 3 },
    ']': { 'opening': '[', 'points': 57 },
    '}': { 'opening': '{', 'points': 1197 },
    '>': { 'opening': '<', 'points': 25137 }
}

points = 0

for line in lines:
    stack = []
    for char in line:
        # print(f'{stack}, {char}')
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            if not stack.pop() == mapping[char]['opening']:
                points += mapping[char]['points']
                break

print(f'Points: {points}')
