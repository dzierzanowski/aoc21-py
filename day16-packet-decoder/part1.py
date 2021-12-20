#!python3

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
        first_bit = '1'
        while first_bit == '1':
            first_bit = data.pop(0)
            del data[:4]  # Unnecessary in part 1
            parsed_bits += 5
        return version
    else:
        # Operator
        l_id = data.pop(0)
        version_sum = 0
        if l_id == '0':
            bits = exint(data[:15])
            del data[:15]
            sub_data = data[:bits]
            del data[:bits]
            while sub_data:
                version_sum += parse_packet(sub_data)
        else:
            packets = exint(data[:11])
            del data[:11]
            for _ in range(0, packets):
                version_sum += parse_packet(data)
        return version + version_sum

result = parse_packet(data)
print(f'Sum of versions: {result}')
