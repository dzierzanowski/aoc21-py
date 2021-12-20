#!python3

with open('input.txt') as file:
    *_, x, y = file.read().split(' ')
    x = [ int(n) for n in x[2:].rstrip(',').split('..') ]
    y = [ int(n) for n in y[2:].split('..') ]
    
x_left, x_right = x
y_bottom, y_top = y

count = 0

# Upper limit for vy from Part 1
for vy_init in range(y_bottom, 86):
    for vx_init in range(0, x_right + 1):
        vx, vy = vx_init, vy_init
        x, y = 0, 0
        while True:
            x_next = x + vx
            y_next = y + vy
            if x_next > x_right or y_next < y_bottom:
                break
            x = x_next
            y = y_next
            if x_left <= x <= x_right and y_bottom <= y <= y_top:
                count += 1
                break
            if vx:
                vx -= 1
            vy -= 1

print(f'Count: {count}')
