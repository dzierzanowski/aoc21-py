#!python3

with open('input.txt') as file:
    template, rules = file.read().split('\n\n')
    template = [c for c in template]
    rules = dict([
        rule.split(' -> ')
        for rule in rules.split('\n')
    ])

for _ in range(0, 10):
    pointer = 0
    while pointer < len(template) - 1:
        first = template[pointer]
        second = template[pointer + 1]
        addition = rules[first + second]
        template.insert(pointer + 1, addition)
        pointer += 2

distinct = set(template)
most_common = 0
least_common = len(template)
for element in distinct:
    count = template.count(element)
    most_common = count if count > most_common else most_common
    least_common = count if count < least_common else least_common

print(f'Result: {most_common - least_common}')