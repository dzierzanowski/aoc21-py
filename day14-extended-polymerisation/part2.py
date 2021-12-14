#!python3

with open('input.txt') as file:
    template, rules = file.read().split('\n\n')
    rules = dict([
        rule.split(' -> ')
        for rule in rules.split('\n')
    ])

counter = {}

for i in range(0, len(template) - 1):
    pair = template[i:i + 2]
    counter[pair] = 1

for _ in range(0, 40):
    new_counter = {}
    for pair in counter:
        count = counter[pair]
        rule = rules[pair]
        new_pair_1 = pair[0] + rule
        new_pair_2 = rule + pair[1]
        if not new_counter.get(new_pair_1):
            new_counter[new_pair_1] = 0
        new_counter[new_pair_1] += counter[pair]
        if not new_counter.get(new_pair_2):
            new_counter[new_pair_2] = 0
        new_counter[new_pair_2] += counter[pair]
    counter = new_counter

print(counter)

element_counter = {}

for key, value in counter.items():
    elem = key[0]
    if not element_counter.get(elem):
        element_counter[elem] = 0
    element_counter[elem] += value
element_counter[template[-1]] += 1 

values = sorted(element_counter.values())
print(f'Result: {values[-1] - values[0]}')
