#!python3

with open('input.txt') as file:
    data = [
        [
            int(c) for c in line
        ]
        for line in file.read().split('\n')
    ]

octopi = {}

# Create data structure for octopi
for y in range(0, 10):
    for x in range(0, 10):
        octopi[(x, y)] = {
            'value': data[y][x],
            'flashed': False
        }

flashes = 0

for _ in range(1, 100 + 1):
    for octopus in octopi.values():
        octopus['value'] += 1
        octopus['flashed'] = False

    flashed = [ key for key in octopi if octopi[key]['value'] > 9 ]
    while flashed:
        for x, y in flashed:
            flashes += 1
            octopi[(x, y)]['value'] = 0
            octopi[(x, y)]['flashed'] = True
            affected = [
                (ax, ay) for ax, ay in octopi
                if not octopi[(ax, ay)]['flashed'] and (abs(ax - x) <= 1 and abs(ay - y) <= 1)
            ]
            for ax, ay in affected:
                octopi[(ax, ay)]['value'] += 1

        flashed = [ key for key in octopi if octopi[key]['value'] > 9 ]

print(f'Flashes after 100 iterations: {flashes}')
