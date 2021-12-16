#!python3

with open('input.txt') as file:
    data = [
        [ int(i) for i in line ]
        for line in file.read().split('\n')
    ]

dimy = len(data)
dimx = len(data[0])
start_point = (0, 0)
final_point = (dimx - 1, dimy - 1)

# Dijkstra
points = {}

for y in range(0, dimy):
    for x in range(0, dimx):
        points[(x, y)] = {
            'val': data[y][x],
            'dist': float('inf'),
            'visited': False
        }
points[start_point]['dist'] = 0
unvisited = set([start_point])

while not points[final_point]['visited']:
    x, y = sorted(unvisited, key=lambda k: points[k]['dist'])[0]
    unvisited.remove((x, y))
    point = points[(x, y)]
    neighbors = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1)
    ]
    neighbors = [
        (x, y) for x, y in neighbors
        if 0 <= x < dimx and 0 <= y < dimy and not points[(x, y)]['visited']
    ]
    for key in neighbors:
        neigh = points[key]
        unvisited.add(key)
        dist = point['dist'] + neigh['val']
        neigh['dist'] = dist if dist < neigh['dist'] else neigh['dist']
    point['visited'] = True

print(f'Distance to target: {points[final_point]["dist"]}')
