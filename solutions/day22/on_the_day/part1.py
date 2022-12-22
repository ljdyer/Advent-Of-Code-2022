from itertools import cycle
import re
from copy import deepcopy

order = {'R': 'RDLUR', 'L': 'RULDR'}

def get_data(real=False):
    if real:
        data_path = '../data.txt'
    else:    
        data_path = '../test_data.txt'
    with open(data_path, 'r') as f:
        data = f.read()
    return data

def next_non_empty(row, start_pos, backwards = False):

    if backwards:
        col = next((i for i in range(start_pos-1, -1, -1) if row[i] != ' '), None)
        if not col:
            col = next((i for i in range(len(row)-1, -1, -1) if row[i] != ' '))
    else:
        col = next((i for i in range(start_pos+1, len(row)) if row[i] != ' '), None)
        if not col:
            col = next((i for i in range(len(row)) if row[i] != ' '))
    return col

def new_orientation(orientation, instruction):

    return order[instruction][order[instruction].index(orientation) + 1]

def go_left(num):

    row, col = pos
    row_ = grid[row]
    for _ in range(num):
        next_col = next_non_empty(row_, col, backwards=True)
        if row_[next_col] == '.':
            col = next_col
        elif row_[next_col] == '#':
            pass
    return (row, col)

def go_right(num):

    row, col = pos
    row_ = grid[row]
    for _ in range(num):
        next_col = next_non_empty(row_, col)
        if row_[next_col] == '.':
            col = next_col
        elif row_[next_col] == '#':
            pass
    return (row, col)

def go_down(num):

    row, col = pos
    col_ = [grid[i][col] for i in range(len(grid))]
    for _ in range(num):
        next_row = next_non_empty(col_, row)
        if col_[next_row] == '.':
            row = next_row
        elif col_[next_row] == '#':
            pass
    return (row, col)

def go_up(num):

    row, col = pos
    col_ = [grid[i][col] for i in range(len(grid))]
    for _ in range(num):
        next_row = next_non_empty(col_, row, backwards=True)
        if col_[next_row] == '.':
            row = next_row
        elif col_[next_row] == '#':
            pass
    return (row, col)

def write_to_file(file_name):

    grid_ = deepcopy(grid)
    row, col = pos
    grid_[row][col] = orientation
    content = '\n'.join([''.join(c for c in row) for row in grid_])
    with open(file_name, 'w') as f:
        f.write(content)


data = get_data(True)
grid, instructions = data.split('\n\n')
grid = [list(g) for g in grid.splitlines()]
row_len = max([len(r) for r in grid])
grid = [r + [' ']*(row_len - len(r)) for r in grid]
print(grid[len(grid) - 1])
print([len(r) for r in grid])
instructions = re.findall(r"[A-Z]|\d+", instructions)
# instructions = ['10', 'L', '5', 'L', '23']
starting_col = next_non_empty(grid[0], 0)
pos = (0, starting_col)
print(pos)
orientation = 'R'
counter = 0
while instructions:
    counter += 1
    instruction = instructions.pop(0)
    if instruction.isnumeric():
        instruction = int(instruction)
        if orientation == 'R':
            pos = go_right(instruction)
        elif orientation == 'D':
            pos = go_down(instruction)
        elif orientation == 'U':
            pos = go_up(instruction)
        elif orientation == 'L':
            pos = go_left(instruction)
    else:
        orientation = new_orientation(orientation, instruction)
    file_name = f'{str(counter).zfill(2)}_{instruction}.txt'
    if counter < 100:
        write_to_file(file_name)

print(pos)
row, col = pos
row += 1
col += 1
print(row, col, orientation)
orientation = {'R': 0, 'D': 1, 'L': 2, 'U': 3}[orientation]
print(f'1000 * {row} + 4 * {col} + {orientation} = {1000 * row + 4 * col + orientation}')



assert new_orientation('U', 'R') == 'R'
assert new_orientation('U', 'L') == 'L'
assert new_orientation('L', 'R') == 'U'

