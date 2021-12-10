#!python3

with open('input.txt') as file:
    measurements = [
        int(line.strip())
        for line in file.readlines()
    ]

prev = measurements.pop(0)
curr = 0
increment_count = 0
while measurements:
    curr = measurements.pop(0)
    increment_count += curr > prev
    prev = curr

print(f"Incrementation count: {increment_count}")

print()
