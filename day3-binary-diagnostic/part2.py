#!python3

with open('input.txt') as file:
    rates = [
        line.strip()
        for line in file.readlines()
    ]

rates_oxy = rates[:]
counter_bits_oxy = [ 0 for i in range(0, len(rates_oxy[0])) ]
pos = 0
while len(rates_oxy) > 1:
    num_bits = len(rates_oxy)
    for rate in rates_oxy:
        if rate[pos] == '1':
            counter_bits_oxy[pos] += 1
    condition = counter_bits_oxy[pos] >= num_bits / 2
    discriminator = '1' if condition else '0'
    rates_oxy = [rate for rate in rates_oxy if rate[pos] == discriminator]
    pos += 1
oxy = rates_oxy[0]
print(oxy)

rates_co2 = rates[:]
counter_bits_co2 = [ 0 for i in range(0, len(rates_co2[0])) ]
pos = 0
while len(rates_co2) > 1:
    num_bits = len(rates_co2)
    for rate in rates_co2:
        if rate[pos] == '1':
            counter_bits_co2[pos] += 1
    condition = counter_bits_co2[pos] < num_bits / 2
    discriminator = '1' if condition else '0'
    rates_co2 = [rate for rate in rates_co2 if rate[pos] == discriminator]
    pos += 1
co2 = rates_co2[0]
print(co2)

result = int(oxy, 2) * int(co2, 2)
print(f'Result: {result}')
