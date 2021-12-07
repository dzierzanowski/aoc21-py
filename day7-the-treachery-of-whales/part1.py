#!python3

with open('input.txt') as file:
    positions = sorted([ int(i) for i in file.read().split(',') ])

l = len(positions)
median = positions[int(l / 2)]
fuel = sum([abs(pos - median) for pos in positions])

print(f"Fuel: {fuel}")
