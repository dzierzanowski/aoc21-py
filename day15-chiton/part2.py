#!python3

with open('input.txt') as file:
    data = [
        [ int(i) for i in line ]
        for line in file.read().split('\n')
    ]

dimy = len(data)
dimx = len(data[0])
start_point = (0, 0)
final_point = (
    dimx * 5 - 1, dimy * 5 - 1
)

# Dijkstra
points = {}

for y in range(0, dimy):
    for x in range(0, dimx):
        for dx in range(0, 5):
            for dy in range(0, 5):
                val = (data[y][x] + dx + dy - 1) % 9 + 1
                cx = x + dx * dimx
                cy = y + dy * dimy
                # print(f'{val}, {cx}, {cy}')
                points[(cx, cy)] = {
                    'val': val,
                    'dist': float('inf'),
                    'visited': False
                }
                
points[start_point]['dist'] = 0
unvisited = set([start_point])

while not points[final_point]['visited']:
    x, y = sorted(unvisited, key=lambda k: points[k]['dist'])[0]
    # print(sorted([val['dist'] for key, val in points.items() if key in unvisited]))
    # print(points[(x, y)]['dist'])
    unvisited.remove((x, y))
    # print(unvisited)
    # print(f'Unvisited count: {len(unvisited)}')
    point = points[(x, y)]
    # print(f'{x}, {y}')
    # print(point)
    neighbors = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1)
    ]
    neighbors = [
        (x, y) for x, y in neighbors
        if 0 <= x < (dimx * 5) and 0 <= y < (dimy * 5) and not points[(x, y)]['visited']
    ]
    # neighbors = [
    #     (key, val) for key, val in points.items()
    #     if not val['visited'] and ((abs(x - key[0]) == 1 and key[1] == y) or (abs(y - key[1]) == 1 and key[0] == x))
    # ]
    # print(neighbors)
    for key in neighbors:
        neigh = points[key]
        unvisited.add(key)
        dist = point['dist'] + neigh['val']
        neigh['dist'] = dist if dist < neigh['dist'] else neigh['dist']
    point['visited'] = True

print(f'Distance to target: {points[final_point]["dist"]}')
