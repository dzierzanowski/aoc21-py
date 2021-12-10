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
    is_const_x = start['x'] == end['x']
    is_const_y = start['y'] == end['y']

    if not is_const_x:
        if start['x'] < end['x']:
            x_axis = range(start['x'], end['x'] + 1)
        else:
            x_axis = list(reversed(range(end['x'], start['x'] + 1)))
        length = len(x_axis)
    if not is_const_y:
        if start['y'] < end['y']:
            y_axis = range(start['y'], end['y'] + 1)
        else:
            y_axis = list(reversed(range(end['y'], start['y'] + 1)))
        length = len(y_axis)

    for i in range(0, length):
        x = start['x'] if is_const_x else x_axis[i]
        y = start['y'] if is_const_y else y_axis[i]
        key = (x, y)
        vent_count[key] = vent_count[key] + 1 if vent_count.get(key) else 1
# print(vent_count)

multivent_point_count = len([ct for ct in vent_count.values() if ct > 1])
print(f"Number of points, where there's more than one vent: {multivent_point_count}")
