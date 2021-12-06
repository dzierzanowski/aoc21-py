#!python3

with open('input.txt') as file:
    fish = [ int(i) for i in file.read().split(',') ]

days = 256

states = [0 for _ in range(0, 9)]

for timer in fish:
    states[timer] += 1

for _ in range(0, days):
    spawning_count = states.pop(0)
    states.append(spawning_count)
    states[6] += spawning_count

print(f'Result: {sum(states)}')
