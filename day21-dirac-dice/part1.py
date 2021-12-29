#!python3

# Offset everything to zero-based indexing

player = {
    0: {
        'pos': 0,
        'score': 0
    },
    1: {
        'pos': 1,
        'score': 0
    }
}

die = 100
rolls = 0
index = 1
while player[0]['score'] < 1000 and player[1]['score'] < 1000:
    rolled = 0
    for _ in range(0, 3):
        die = die % 100 + 1
        rolled += die
        rolls += 1
    index ^= 1
    p = player[index]
    pos = (p['pos'] + rolled) % 10
    p['pos'] = pos
    p['score'] += pos + 1

result = rolls * min([ p['score'] for p in player.values() ])
print(f'Result: {result}')
