#!python3
import sys

with open('input.txt') as file:
    hits, *boards = file.read().split('\n\n')
    hits = [ int(hit) for hit in hits.split(',') ]

best_board_steps = 0
best_board_score = sys.maxsize

for board in boards:
    field_map   = {}
    column_hits = [0 for _ in range(0, 5)]
    row_hits    = [0 for _ in range(0, 5)]
    steps       = 0
    last_hit    = None
    board = [
        [ int(field) for field in line.split(' ') if field != '' ]
        for line in board.splitlines()
    ]
    for y in range(0, 5):
        for x in range(0, 5):
            field_map[board[y][x]] = (x, y)
    for hit in hits:
        steps += 1
        if hit in field_map.keys():
            x, y = field_map[hit]
            column_hits[x] += 1
            row_hits[y] += 1
            del field_map[hit]
            if 5 in column_hits or 5 in row_hits:
                last_hit = hit
                break
    
    score = last_hit * sum(field_map.keys())
    if (steps > best_board_steps) or (steps == best_board_steps and score < best_board_score):
        best_board_steps = steps
        best_board_score = score

print(f"Steps: {best_board_steps}")
print(f"Score: {best_board_score}")
