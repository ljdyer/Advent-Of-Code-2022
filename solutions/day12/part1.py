import string
from numpy import inf
from random import shuffle
letters = list(string.ascii_lowercase)
order = {letter: number for number, letter in enumerate(letters)}

with open('test_data.txt', 'r') as f:
# with open('../data.txt', 'r') as f:
    grid = [list(r) for r in f.read().splitlines()]


def print_grid(grid):

    for r in grid:
        print('\t'.join(map(str, r)))


num_rows = len(grid)
num_cols = len(grid[0])
Sx = [r for r in enumerate(grid) if 'S' in r[1]][0][0]
Sy = grid[Sx].index('S')
S = (Sx, Sy)
print(S)
grid[Sx][Sy] = 'a'
Ex = [r for r in enumerate(grid) if 'E' in r[1]][0][0]
Ey = grid[Ex].index('E')
E = (Ex, Ey)
print(E)
grid[Ex][Ey] = 'z'

grid = [[order[x] for x in r] for r in grid]
print_grid(grid)

def neighbours(point):
    x, y = point
    if x > 0:
        yield (x-1, y)
    if x < num_rows-1:
        yield (x+1, y)
    if y > 0:
        yield (x, y-1)
    if y < num_cols-1:
        yield (x, y+1)

def movable_neighbours(current_point):
    neighbours_ = neighbours(current_point)
    mn = []
    Cx, Cy = current_point
    for n in neighbours_:
        Nx, Ny = n
        try:
            if grid[Cx][Cy] - grid[Nx][Ny] >= -1:
                mn.append(n)
        except:
            print(n)
            quit()
    shuffle(mn)
    return mn
    
# print(list(neighbours(E)))

# def get_min_recursively(current_pos, num_steps, points_visited=None, min=inf):

#     if points_visited is None:
#         points_visited = []
#     if num_steps > min:
#         return
#     if num_steps > 40:
#         return
#     elif current_pos == E:
#         print('MADE IT!!!')
#         min = num_steps
#         return num_steps
#     else:
#         movable_neighbours_ = movable_neighbours(current_pos)
#         points_visited.append(current_pos)
#         print(current_pos, movable_neighbours_)
#         movable_neighbours_ = [m for m in movable_neighbours_ if m not in points_visited]
#         print(movable_neighbours_)
#         if E in movable_neighbours_:
#             print('Nearly there...')
#         for n in movable_neighbours_:
#             print(n, num_steps+1, points_visited, min)
#             get_min_recursively(n, num_steps+1, points_visited, min)
#     return min

min = inf
current_pos = S
visited = []
so_far = [((0,0), [])]
steps = 0
# while min==inf:
for i in range(50):
    next_ = []
    steps += 1
    for pos, visited in so_far:
        if pos == E:
            pass
            # print(steps)
        mn = [n for n in movable_neighbours(pos) if n not in visited]
        for n in mn:
            next_.append((n, visited+[pos]))
    so_far = next_
    print(len(so_far))
# print(so_far)

    



# print(get_min_recursively((0,0), 0))
# for m in min:
    # print(m)
# print(next(min))
# print(movable_neighbours((3,2)))