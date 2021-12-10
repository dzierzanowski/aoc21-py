#!python3

with open('input.txt') as file:
    data = [
        [ int(c) for c in line ]
        for line in file.read().split('\n')
    ]

dim_y = len(data)
dim_x = len(data[0])

low_points = {}

for y in range(0, dim_y):
    for x in range(0, dim_x):
        h = data[y][x]
        if not y - 1 < 0      and h >= data[y - 1][x]:
            continue
        if not y + 1 >= dim_y and h >= data[y + 1][x]:
            continue
        if not x - 1 < 0      and h >= data[y][x - 1]:
            continue
        if not x + 1 >= dim_x and h >= data[y][x + 1]:
            continue
        low_points[(x, y)] = h

risk = sum(low_points.values()) + len(low_points)
print(f'Risk: {risk}')
