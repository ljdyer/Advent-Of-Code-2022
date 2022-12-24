from math import inf
from itertools import count

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

def draw():

    print(''.join(['#'] + [' '] + ['#']*(num_cols)))
    for r in range(num_rows):
        this_row = '#'
        for c in range(num_cols):
            if len(blizzards[(r, c)]) == 0:
                this_row = this_row + '.'
            elif len(blizzards[(r, c)]) == 1:
                this_row = this_row + blizzards[(r, c)][0]
            elif len(blizzards[(r, c)]) > 1:
                this_row = this_row + str(len(blizzards[(r, c)]))
        this_row = this_row + '#'
        print(this_row)
    print(''.join(['#']*(num_cols) + [' '] + ['#']))
    print()



def next_pos(pos, dir):

    row, col = pos
    if dir == '>':
        return (row, 0) if col == num_cols - 1 else (row, col+1)
    elif dir == '<':
        return (row, num_cols-1) if col == 0 else (row, col-1)
    elif dir == 'v':
        return (0, col) if row == num_rows-1 else (row+1, col)
    elif dir == '^':
        return (num_rows-1, col) if row == 0 else (row-1, col)
    else:
        print(dir)
            

def move_blizzards():

    new_blizzards = {(row, col): [] for row in range(num_rows) for col in range(num_cols)}
    for p, b in blizzards.items():
        for b_ in b:
            next_pos_ = next_pos(p, b_)
            new_blizzards[next_pos_].append(b_)
    return new_blizzards

def get_neighbours(pos):

    row, col = pos
    neighbours = []
    if row != 0:
        neighbours.append((row-1, col))
    if row != num_rows-1:
        neighbours.append((row+1, col))
    if col != 0:
        neighbours.append((row, col-1))
    if col != num_cols-1:
        neighbours.append((row, col+1))
    return neighbours


data = get_data('test').splitlines()
area = [list(l.strip('#')) for l in data[1:-1]]
print(area)
num_cols = len(area[0])
num_rows = len(area)
blizzards = {(row, col): [] if area[row][col] == '.' else [area[row][col]]
             for row in range(num_rows) for col in range(num_cols)}
blizzard_states = []

for i in range(1, 1000):
    blizzards = move_blizzards()
    blizzard_states.append(blizzards)

unvisited = set(x for x in blizzards.keys())
tentative_distance = {x: inf for x in unvisited}
# 0,0
next_neighbours = [(0,0)]
for n in next_neighbours:
    cost = next(i for i in count(start=1, step=1) if blizzard_states[i][n] == [])
    tentative_distance[n] = min(tentative_distance[n], cost)
# neighbours
next_neighbours = get_neighbours((0,0))
for n in next_neighbours:
    cost = next(i for i in count(start=tentative_distance[(0,0)]+1, step=1) if blizzard_states[i][n] == [])
    tentative_distance[n] = min(tentative_distance[n], cost)
unvisited.remove((0,0))

destination = (num_rows-1, num_cols-1)
for z in range(50):
    next_ = min([(k, v) for k,v in tentative_distance.items() if k in unvisited], key=lambda x: x[1])[0]
    next_neighbours = get_neighbours(next_)
    for n in next_neighbours:
        cost = next(i for i in count(start=tentative_distance[next_]+1, step=1) if blizzard_states[i][n] == [])
        tentative_distance[n] = min(tentative_distance[n], cost)
    unvisited.remove(next_)
    if destination not in unvisited:
        print(tentative_distance[destination])
        break

# print(list((k, v) for k, v in tentative_distance.items() if v != inf))