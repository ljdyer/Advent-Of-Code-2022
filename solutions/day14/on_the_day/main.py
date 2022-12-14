import traceback

with open('../test_data.txt', 'r') as f:
# with open('data.txt', 'r') as f:
    data = f.read().splitlines()

def join_the_dots(lis_):
    pairs = [lis_[i: i+2] for i in range(len(lis_)-1)]
    points = []
    for p0, p1 in pairs:
        x0, y0 = p0
        x1, y1 = p1
        if x0 == x1:
            if y0 < y1:
                points.extend([(x0, y) for y in range(y0, y1+1)])
            elif y1 < y0:
                points.extend([(x0, y) for y in range(y1, y0+1)])
            else:
                raise ValueError()
        elif y0 == y1:
            if x0 < x1:
                points.extend([(x, y0) for x in range(x0, x1+1)])
            elif x1 < x0:
                points.extend([(x, y0) for x in range(x1, x0+1)])
            else:
                raise ValueError()
        else:
            raise ValueError()
    return list(set(points))




lines = [[eval(a.strip()) for a in l.split('->')] for l in data]
num_cols, num_rows = max([c[0] for l in lines for c in l]), max([c[1] for l in lines for c in l])
grid = [['.' for y in range(num_cols+1)] for x in range(num_rows+1)]


def print_range(grid, f, t):
    print('\t'.join(['.'] + list(map(str, range(f, t+1)))))
    for i, g in enumerate(grid):
        print('\t'.join(
            [str(i)] + g[f: t+1]
        ))


def move_sand(grid, sx, sy):

    try:
        while grid[sx+1][sy] == '.':
            sx += 1
        if grid[sx+1][sy-1] == '.':
            return move_sand(grid, sx, sy-1)
        elif grid[sx+1][sy+1] == '.':
            return move_sand(grid, sx, sy+1)
        else:
            return sx, sy
    except Exception as e:
        return None


def add_sand(grid):

    grid_ = grid.copy()
    sx, sy = 0, 500
    new_sand_pos = move_sand(grid, sx, sy)
    if new_sand_pos:
        sx_, sy_ = new_sand_pos
        grid_[sx_][sy_] = 'o'
        return(grid_)
    else:
        return None


rocks = [r for l in lines for r in join_the_dots(l)]
# print(rocks)
for x,y in rocks:
    grid[y][x] = '#'
# print_range(grid, 490, 503)

for i in range(5000):
    grid = add_sand(grid)
    if grid is None:
        print(i)
        break
    
    # print_range(grid, 490, 503)