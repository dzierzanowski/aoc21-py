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

basins = []
for point in low_points.keys():
    stack = set([ point ])  # Start with a low point
    basin_size = 0
    while stack:
        print(stack)
        x, y = stack.pop()  # Get a point
        basin_size += 1
        cur = data[y][x]  # Get its height
        # Inspect adjacent points
        adj_points = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for adj_x, adj_y in adj_points:
            # If OOB, skip
            if not (0 <= adj_x < dim_x and 0 <= adj_y < dim_y):
                continue
            adj = data[adj_y][adj_x]
            # If between 9 and current point, add to basin (stack of points)
            if adj < 9 and not adj < cur:
                stack.add((adj_x, adj_y))
        # Elevate the current point to a high point to avoid loops
        data[y][x] = 9
    basins.append(basin_size)

product = 1
for basin in list(reversed(sorted(basins)))[:3]:
    product *= basin

print(f'Result: {product}')
