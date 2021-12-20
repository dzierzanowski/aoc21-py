#!python3
from functools import reduce

with open('input.txt') as file:
    data = [
        b for b in ''.join([
            f'{int(i, 16):04b}' for i in file.read()
        ])
    ]

def join(array):
    return ''.join(array)

def exint(array):
    return int(join(array), 2)

def parse_packet(data):
    version = exint(data[:3])
    type_id = exint(data[3:6])
    del data[:6]
    parsed_bits = 6
    if type_id == 4:
        # Literal value
        val = None
        val_str = ''
        first_bit = '1'
        while first_bit == '1':
            first_bit = data.pop(0)
            val_str += join(data[:4])
            del data[:4]
            parsed_bits += 5
        val = int(val_str, 2)
        # For part 1, return just the version number
        return val
    else:
        # Operator
        l_id = data.pop(0)
        sub_values = []
        if l_id == '0':
            bits = exint(data[:15])
            del data[:15]
            sub_data = data[:bits]
            del data[:bits]
            while sub_data:
                sub_values.append(parse_packet(sub_data))
        else:
            packets = exint(data[:11])
            del data[:11]
            for _ in range(0, packets):
                sub_values.append(parse_packet(data))
        if type_id == 0:
            return sum(sub_values)
        elif type_id == 1:
            return reduce(lambda x, y: x * y, sub_values, 1)
        elif type_id == 2:
            return min(sub_values)
        elif type_id == 3:
            return max(sub_values)
        elif type_id == 5:
            return int(sub_values[0] > sub_values[1])
        elif type_id == 6:
            return int(sub_values[1] > sub_values[0])
        else:
            return int(sub_values[0] == sub_values[1])

result = parse_packet(data)
print(f'Result: {result}')
