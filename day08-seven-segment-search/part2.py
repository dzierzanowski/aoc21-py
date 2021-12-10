#!python3

with open('input.txt') as file:
    entries = [
        [
            [
                frozenset(word)
                for word in half.split(' ')
            ]
            for half in line.strip().split(' | ')
        ]
        for line in file.readlines()
    ]

sum_digits = 0

for entry in entries:
    seq = entry[0]

    one =   [ word for word in seq if len(word) == 2 ][0]
    seven = [ word for word in seq if len(word) == 3 ][0]
    four =  [ word for word in seq if len(word) == 4 ][0]
    eight = [ word for word in seq if len(word) == 7 ][0]
    # Map word for digit
    m = {
        one: '1',
        four: '4',
        seven: '7',
        eight: '8'
    }

    rest = set(seq) - set([one, four, seven, eight])
    for word in rest:
        # 0, 2, 3, 5, 6, 9
        if len(word & one) == 2:
            # 0, 3, 9
            if len(word - four) == 3:
                m[word] = '0'
            elif len(word - seven) == 2:
                m[word] = '3'
            else:
                m[word] = '9'
        else:
            # 2, 5, 6
            if len(word - four) == 2:
                m[word] = '5'
            elif len(word - seven) == 3:
                m[word] = '2'
            else:
                m[word] = '6'

    val = ''
    display = entry[1]
    for digit in display:
        val += m[digit]

    sum_digits += int(val)

print(f'Result: {sum_digits}')
