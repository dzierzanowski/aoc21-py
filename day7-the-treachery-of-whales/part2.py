#!python3

with open('input.txt') as file:
    positions = [ int(i) for i in file.read().split(',') ]

tri = lambda n: int((n + 1) * n / 2)

s = sum(positions)
l = len(positions)
avg = int(s / l)

fuel = sum([tri(abs(pos - avg)) for pos in positions])

print(f"Fuel: {fuel}")
