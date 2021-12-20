#!python3

with open('input.txt') as file:
    pairs = [
        eval(line)  # Nice
        for line in file.read().split('\n')
    ]

def explode(pair, level):
    if isinstance(pair, int):
        return None

    left, right = pair

    if level == 3:
        if isinstance(left, list):
            if isinstance(right, list):
                right[0] += left[1]
            else:
                pair[1] += left[1]
            pair[0] = 0
            return left[0], 'left'
        elif isinstance(right, list):
            pair[0] += right[0]
            pair[1] = 0
            return right[1], 'right'

    result_left = explode(left, level + 1)
    if result_left:
        value, direction = result_left
        if direction in ('left', 'exit'):
            return value, direction
        elif isinstance(right, int):
            pair[1] += value
            return 0, 'exit'
        else:
            parent = right
            while isinstance(parent[0], list):
                parent = parent[0]
            parent[0] += value
            return 0, 'exit'

    result_right = explode(right, level + 1)
    if result_right:
        value, direction = result_right
        if direction in ('right', 'exit'):
            return value, 'right'
        elif isinstance(left, int):
            pair[0] += value
            return 0, 'exit'
        else:
            parent = left
            while isinstance(parent[1], list):
                parent = parent[1]
            parent[1] += value
            return 0, 'exit'
    return None

def split(pair):
    left, right = pair
    if isinstance(left, int):
        if left >= 10:
            pair[0] = [ int(left / 2), int((left + 1) / 2) ]
            return True
    else:
        if split(left):
            return True
    if isinstance(right, int):
        if right >= 10:
            pair[1] = [ int(right / 2), int((right + 1) / 2) ]
            return True
    else:
        if split(right):
            return True
    return False

def magnitude(pair):
    if isinstance(pair, int):
        return pair
    left, right = pair
    return 3 * magnitude(left) + 2 * magnitude(right)

snail_sum = pairs.pop(0)
while pairs:
    next_pair = pairs.pop(0)
    snail_sum = [ snail_sum, next_pair ]
    while explode(snail_sum, 0) or split(snail_sum):
        pass
result = magnitude(snail_sum)
print(f'Magnitude: {result}')
