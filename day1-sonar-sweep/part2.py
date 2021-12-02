#!python3

with open('input.txt') as file:
    measurements = [
        int(line.strip())
        for line in file.readlines()
    ]

prev = sum(measurements[:3])
curr = 0
increment_count = 0
while len(measurements) > 3:
    measurements.pop(0)
    curr = sum(measurements[:3])
    increment_count += curr > prev
    prev = curr

print(f"Incrementation count: {increment_count}")
