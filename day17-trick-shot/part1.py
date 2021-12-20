#!python3

with open('input.txt') as file:
    *_, x, y = file.read().split(' ')
    x = [ int(n) for n in x[2:].rstrip(',').split('..') ]
    y = [ int(n) for n in y[2:].split('..') ]
    
x_left, x_right = x
y_bottom, y_top = y

# x is irrelevant in this part
vy_init = 0
result = 0

while True:
    y = 0
    vy = vy_init
    y_max = 0
    while True:
        next_y = y + vy
        if next_y < y_bottom:
            break
        y = next_y
        vy -= 1
        y_max = y if y > y_max else y_max
    if y == 0:
        # All launches eventually go back to y = 0. At one point, the next step
        # after that will always be beyond lower boundary.
        break
    result = y_max
    vy_init += 1

print(f'Max y: {result} (initial vy: {vy_init - 1})')
