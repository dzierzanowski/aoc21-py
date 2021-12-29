#!python3

wins = {
    0: 0,
    1: 0
}
p1_wins = 0
p2_wins = 0

def play_round(wins, index, p1_pos, p1_score, p2_pos, p2_score, worlds, next_roll):
    if index == 0:
        p1_pos = (p1_pos + next_roll) % 10
        p1_score += p1_pos + 1
        if p1_score >= 21:
            wins[index] += worlds
            return
    else:
        p2_pos = (p2_pos + next_roll) % 10
        p2_score += p2_pos + 1
        if p2_score >= 21:
            wins[index] += worlds
            return
    possibilities = [ sum([i, j, k]) for i in range(1, 4) for j in range(1, 4) for k in range(1, 4) ]
    for i in set(possibilities):
        count = possibilities.count(i)
        play_round(wins, index ^ 1, p1_pos, p1_score, p2_pos, p2_score, worlds + count, i)

possibilities = [ sum([i, j, k]) for i in range(1, 4) for j in range(1, 4) for k in range(1, 4) ]
for i in set(possibilities):
    count = possibilities.count(i)
    play_round(wins, 0, 1, 0, 2, 0, count, i)

result = max(wins.values())
print(f'Most wins: {result}')
