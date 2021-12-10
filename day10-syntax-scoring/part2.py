#!python3

with open('input.txt') as file:
    lines = file.read().split('\n')

mapping = {
    ')': { 'opening': '(', 'points': 1 },
    ']': { 'opening': '[', 'points': 2 },
    '}': { 'opening': '{', 'points': 3 },
    '>': { 'opening': '<', 'points': 4 }
}

scores = []

for line in lines:
    stack = []
    legit = True
    for char in line:
        # print(f'{stack}, {char}')
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            if not stack.pop() == mapping[char]['opening']:
                legit = False
                break
    if legit:
        points = 0
        for char in reversed(stack):
            points *= 5
            points += [
                mapping[key]['points']
                for key in mapping
                if mapping[key]['opening'] == char
            ][0]
        scores.append(points)

middle = sorted(scores)[int(len(scores) / 2)]

print(f'Middle score: {middle}')
