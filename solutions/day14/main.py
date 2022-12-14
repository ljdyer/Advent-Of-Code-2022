from itertools import count
from copy import deepcopy

with open('data.txt', 'r') as f:
    data = f.read().splitlines()


# ====================
def rock_positions(rock_lines):
    pairs = [rock_lines[i: i+2] for i in range(len(rock_lines)-1)]
    points = []
    for p0, p1 in pairs:
        x0, y0, x1, y1 = *p0, *p1
        if x0 == x1:
            points.extend([(x0, y) for y in range(min(y0, y1), max(y0, y1) + 1)])
        else:
            points.extend([(x, y0) for x in range(min(x0, x1), max(x0, x1) + 1)])
    return list(set(points))


# ====================
def move_sand(grid, sx, sy):

    try:
        while grid[sx+1][sy] == '.':
            # Fall vertically
            sx += 1
        if grid[sx+1][sy-1] == '.':
            # Fall diagonally down+left and continue falling
            return move_sand(grid, sx, sy-1)
        elif grid[sx+1][sy+1] == '.':
            # Fall diagonally down+right and continue falling
            return move_sand(grid, sx, sy+1)
        else:
            return sx, sy
    except Exception as e:
        # Off the grid!
        print(num_sand_units)
        # None signals to main part of program to stop
        return None

# ====================
def add_sand(grid):

    sx, sy = 0, 500
    sand_pos = move_sand(grid, sx, sy)
    if not sand_pos:
        return None
    sx_, sy_ = sand_pos
    if (sx_, sy_) == (0, 500):
        # Last unit of sand came to rest at (0, 500)!
        print(num_sand_units + 1)
        quit()
    grid[sx_][sy_] = 'o'
    return grid


lines = [[eval(a.strip()) for a in l.split('->')] for l in data]
num_cols, num_rows = max([c[0] for l in lines for c in l]), max([c[1] for l in lines for c in l])
grid = [['.' for _ in range(num_cols+1)] for _ in range(num_rows+1)]
rocks = [r for l in lines for r in rock_positions(l)]
for x,y in rocks:
    grid[y][x] = '#'

# # Part 1
grid_ = deepcopy(grid)
for num_sand_units in count(start=0, step=1):
    if grid_:
        grid_ = add_sand(grid_)
    else:
        break

# Part 2
grid.append(['.'] * (num_cols+1))
grid = [r + ['.']*1000 for r in grid]
grid.append(['#'] * (num_cols+1001))
for num_sand_units in count(start=0, step=1):
    grid = add_sand(grid)