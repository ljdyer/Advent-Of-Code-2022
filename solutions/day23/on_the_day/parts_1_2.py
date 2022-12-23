from time import time

def get_data(which: str = 'test'):
    if which == 'real':
        data_path = '../data.txt'
    elif which == 'test2':
        data_path = '../test_data_2.txt'
    else:    
        data_path = '../test_data.txt'
    with open(data_path, 'r') as f:
        data = f.read()
    return data

from itertools import cycle
positions = cycle(['N', 'S', 'W', 'E'])


data = get_data('real').splitlines()
# data = get_data('test').splitlines()
# data = get_data('test2').splitlines()

elves = [(h,i) for h, row in enumerate(data) for i in range(len(row)) if data[h][i] == '#']
# print(elves)

def decide_position(elf, first_position):

    row, col = elf
    # print(first_position)
    if all((i, j) not in elves for i, j in 
    [
        (row+1, col), (row+1, col-1), (row+1, col+1),
        (row-1, col), (row-1, col-1), (row-1, col+1),
        (row, col-1), (row, col+1)
    ]
    ):
        return (row, col)
    else:
        if first_position == 'N':
            if (row-1, col-1) not in elves and (row-1, col) not in elves and (row-1, col+1) not in elves:
                return (row-1, col)
            elif (row+1, col-1) not in elves and (row+1, col) not in elves and (row+1, col+1) not in elves:
                return (row+1, col)
            elif (row-1, col-1) not in elves and (row, col-1) not in elves and (row+1, col-1) not in elves:
                return (row, col-1)
            elif (row-1, col+1) not in elves and (row, col+1) not in elves and (row+1, col+1) not in elves:
                return (row, col+1)
            else:
                return (row, col)
                print(row, col)
                raise ValueError
        if first_position == 'S':
            if (row+1, col-1) not in elves and (row+1, col) not in elves and (row+1, col+1) not in elves:
                return (row+1, col)
            elif (row-1, col-1) not in elves and (row, col-1) not in elves and (row+1, col-1) not in elves:
                return (row, col-1)
            elif (row-1, col+1) not in elves and (row, col+1) not in elves and (row+1, col+1) not in elves:
                return (row, col+1)
            elif (row-1, col-1) not in elves and (row-1, col) not in elves and (row-1, col+1) not in elves:
                return (row-1, col)
            else:
                return (row, col)
                raise ValueError
        if first_position == 'W':
            if (row-1, col-1) not in elves and (row, col-1) not in elves and (row+1, col-1) not in elves:
                return (row, col-1)
            elif (row-1, col+1) not in elves and (row, col+1) not in elves and (row+1, col+1) not in elves:
                return (row, col+1)
            elif (row-1, col-1) not in elves and (row-1, col) not in elves and (row-1, col+1) not in elves:
                return (row-1, col)
            elif (row+1, col-1) not in elves and (row+1, col) not in elves and (row+1, col+1) not in elves:
                return (row+1, col)
            else:
                return (row, col)
                raise ValueError
        if first_position == 'E':
            if (row-1, col+1) not in elves and (row, col+1) not in elves and (row+1, col+1) not in elves:
                return (row, col+1)
            elif (row-1, col-1) not in elves and (row-1, col) not in elves and (row-1, col+1) not in elves:
                return (row-1, col)
            elif (row+1, col-1) not in elves and (row+1, col) not in elves and (row+1, col+1) not in elves:
                return (row+1, col)
            elif (row-1, col-1) not in elves and (row, col-1) not in elves and (row+1, col-1) not in elves:
                return (row, col-1)
            else:
                return (row, col)
                raise ValueError


def get_grid():

    rows = [i for i,_ in elves]
    cols = [j for _,j in elves]
    max_row, min_row = (max(rows), min(rows))
    max_col, min_col = (max(cols), min(cols))
    # print(min_row, max_row, min_col, max_col)
    rows = [['#' if (row, col) in elves else '.' for col in range(min_col, max_col+1)] for row in range(min_row, max_row+1)]
    rows = [''.join(row) for row in rows]
    return rows


def print_grid():

    rows = get_grid()
    for r in rows:
        print(r)


def save_grid():

    rows = get_grid()
    grid = '\n'.join(rows)
    with open('grid.txt', 'w') as f:
        f.write(grid)


def count_empty():

    rows = get_grid()
    return ''.join(rows).count('.')

start_time = time()
print(start_time)
# print(elves)
print(len(elves))
for round in range(1, 1_000_001):
    first_position = next(positions)
    proposed_positions = [decide_position(elf, first_position) for elf in elves]
    prev_elves = elves
    elves = [proposed_positions[i] if proposed_positions.count(proposed_positions[i]) == 1 else elves[i] for i in range(len(elves))]
    number_moving = len(elves) - len([i for i in range(len(elves)) if elves[i] == prev_elves[i]])
    print(round, ':', number_moving)
    if number_moving == 0:
        print()
        print(round)
        break
    # print_grid()
    # print()


# print(elves)
end_time = time()
print(end_time - start_time)
save_grid()
# print(count_empty())



