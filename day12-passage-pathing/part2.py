#!python3

with open('input.txt') as file:
    links = [
        line.split('-')
        for line in file.read().split('\n')
    ]

nodes = {}

for link in links:
    start, end = link
    if start not in nodes:
        nodes[start] = {
            'small': start.islower(),
            'neighbors': []
        }
    if end not in nodes:
        nodes[end] = {
            'small': end.islower(),
            'neighbors': []
        }
    nodes[start]['neighbors'].append(end)
    nodes[end]['neighbors'].append(start)

paths = []

candidates = [
    [ 'start' ]
]
while candidates:
    curr = candidates.pop()
    last = curr[-1]
    for neigh in nodes[last]['neighbors']:
        small_caves = [n for n in curr if n.islower()]
        if neigh == 'start':
            pass
        elif neigh == 'end':
            paths.append(curr.copy() + [ 'end' ])
        elif (neigh not in curr) or (len(small_caves) == len(set(small_caves))) or (not nodes[neigh]['small']):
            candidates.append(curr.copy() + [ neigh ])

print(f'Path count: {len(paths)}')
