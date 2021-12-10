#!python3

with open('input.txt') as file:
    rates = [
        line.strip()
        for line in file.readlines()
    ]

num_bits = len(rates[0])
# Gamma
counter_bits = [ 0 for i in range(0, num_bits) ]

for rate in rates:
    for i in range(0, num_bits):
        if rate[i] == '1':
            counter_bits[i] += 1

gamma = ''
epsilon = ''
rate_count = len(rates)
for count in counter_bits:
    if count > rate_count / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

result = int(gamma, 2) * int(epsilon, 2)
print(f'Result: {result}')
