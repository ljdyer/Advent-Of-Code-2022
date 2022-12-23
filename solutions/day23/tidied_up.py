from itertools import cycle
from time import time

directions = ['N', 'S', 'W', 'E']

# ====================
def get_elves():
    with open('data.txt', 'r') as f:
        data = f.read().splitlines()
    elves = set([(h,i) for h, row in enumerate(data)
                 for i in range(len(row)) if data[h][i] == '#'])
    return elves


# ====================
def decide_position(elf, first_direction):

    row, col = elf
    all_surrounding = [(x, y) for x in range(row-1, row+2) for y in range (col-1, col+2) if (x, y) != (row, col)]
    if all((i, j) not in elves for i, j in all_surrounding):
        return (row, col)
    else:
        checks = {
            'N': [set(((row-1, y) for y in range(col-1, col+2))), (row-1, col)],
            'S': [set(((row+1, y) for y in range(col-1, col+2))), (row+1, col)],
            'W': [set(((x, col-1) for x in range(row-1, row+2))), (row, col-1)],
            'E': [set(((x, col+1) for x in range(row-1, row+2))), (row, col+1)]
        }
        check_order = directions[directions.index(first_direction):] + directions[:directions.index(first_direction)]
        for direction in check_order:
            if all(elf not in elves for elf in checks[direction][0]):
                return checks[direction][1]
        else:
            return (row, col)


# ====================
def count_empty():

    rows = [i for i,_ in elves]
    cols = [j for _,j in elves]
    max_row, min_row = (max(rows), min(rows))
    max_col, min_col = (max(cols), min(cols))
    total_space = (max_row + 1 - min_row) * (max_col + 1 - min_col)
    empty_space = total_space - len(elves)
    return empty_space


# Part 1
elves = get_elves()
start_time = time()
first_directions = cycle(directions)
for round in range(1, 11):
    move_positions = {}
    stay = []
    first_direction = next(first_directions)
    for elf in elves:
        proposed_position = decide_position(elf, first_direction)
        if proposed_position not in move_positions.keys():
            move_positions[proposed_position] = elf
        else:
            stay.append(elf)
            stay.append(move_positions[proposed_position])
            del move_positions[proposed_position]
    elves = set(list(move_positions.keys()) + stay)
answer = count_empty()
end_time = time()
time_taken = end_time - start_time
print(f'Part 1 answer: {answer} (time taken: {time_taken:.2f}s')

# Part 2
elves = get_elves()
start_time = time()
first_directions = cycle(directions)
num_elves = len(elves)
for round in range(1, 1_000_001):
    prev_elves = elves
    move_positions = {}
    stay = []
    first_direction = next(first_directions)
    for elf in elves:
        proposed_position = decide_position(elf, first_direction)
        if proposed_position not in move_positions.keys():
            move_positions[proposed_position] = elf
        else:
            stay.append(elf)
            stay.append(move_positions[proposed_position])
            del move_positions[proposed_position]
    elves = set(list(move_positions.keys()) + stay)
    if len(prev_elves.intersection(elves)) == num_elves:
        answer = round
        break
end_time = time()
time_taken = end_time - start_time
print(f'Part 2 answer: {answer} (time taken: {time_taken:.2f}s')
