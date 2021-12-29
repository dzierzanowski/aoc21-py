#!python3

with open('input.txt') as file:
    algorithm, source = file.read().split('\n\n')
    source = [
        [
            c == '#'
            for c in line
        ]
        for line in source.split('\n')
    ]

image = {}

for y in range(0, len(source)):
    line = source[y]
    for x in range(0, len(line)):
        image[(x, y)] = line[x]

for _ in range(0, 50):
    x_list = [ x for x, y in image ]
    y_list = [ y for x, y in image ]
    min_x, max_x = min(x_list) - 1, max(x_list) + 1
    min_y, max_y = min(y_list) - 1, max(y_list) + 1

    value_for_none = algorithm[0] == '#' and _ % 2

    new_image = {}

    for x, y in [ (x, y) for y in range(min_y, max_y + 1) for x in range(min_x, max_x + 1) ]:
        raw = [ image.get((subx, suby)) for suby in range(y - 1, y + 2) for subx in range(x - 1, x + 2) ]
        raw = [ val if val != None else value_for_none for val in raw ]
        number_str = ''.join([ '1' if obj else '0' for obj in raw ])
        # print(number_str)
        number = int(number_str, 2)
        val = algorithm[number] == '#'
        # print(val)
        new_image[(x, y)] = val
    image = new_image

x_list = [ x for x, y in image ]
y_list = [ y for x, y in image ]
min_x, max_x = min(x_list) - 1, max(x_list) + 1
min_y, max_y = min(y_list) - 1, max(y_list) + 1
print(f'minx {min_x} maxx {max_x} miny {min_y} maxy {max_y}')

result = sum(image.values())
print(f'Result: {result}')
