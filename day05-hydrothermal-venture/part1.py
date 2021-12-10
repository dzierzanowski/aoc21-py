#!python3

with open('input.txt') as file:
    lines = [
        [
            {
                'x': int(pair.split(',')[0]),
                'y': int(pair.split(',')[1])
            }
            for pair in line.strip().split(' -> ')
        ]
        for line in file.readlines()
    ]

vent_count = {}

for line in lines:
    start = line[0]
    end   = line[1]

    if start['x'] == end['x']:
        axis = 'y'

    elif line[0]['y'] == line[1]['y']:
        axis = 'x'
    else:
        continue  # Filter out only horizontal & vertical lines

    bound = sorted([ start[axis], end[axis] ])
    for i in range(bound[0], bound[1] + 1):
        if axis == 'x':
            key = (i, start['y'])
        else:
            key = (start['x'], i)
        vent_count[key] = vent_count[key] + 1 if vent_count.get(key) else 1

multivent_point_count = len([ct for ct in vent_count.values() if ct > 1])
print(f"Number of points, where there's more than one vent: {multivent_point_count}")
