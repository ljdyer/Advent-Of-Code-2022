import string
from numpy import inf
from random import shuffle
letters = list(string.ascii_lowercase)
order = {letter: number for number, letter in enumerate(letters)}

# with open('test_data.txt', 'r') as f:
with open('data.txt', 'r') as f:
    grid = [list(r) for r in f.read().splitlines()]

num_rows = len(grid)
num_cols = len(grid[0])
Sx = [r for r in enumerate(grid) if 'S' in r[1]][0][0]
Sy = grid[Sx].index('S')
S = (Sx, Sy)
grid[Sx][Sy] = 'a'
Ex = [r for r in enumerate(grid) if 'E' in r[1]][0][0]
Ey = grid[Ex].index('E')
E = (Ex, Ey)
grid[Ex][Ey] = 'z'

grid = [[order[x] for x in r] for r in grid]

def height(point):
    x,y = point
    try:
        return grid[x][y]
    except:
        return inf

def unvisited_neighbours(current_point, unvisited):
    x,y = current_point
    return [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
        if height(n) < height(current_point) + 2 and n in unvisited]
    
def get_shortest_path(S):
    unvisited = {(x, y) for x in range(num_rows) for y in range(num_cols)}
    tentative_distance = {node: inf for node in unvisited}
    tentative_distance[S] = 0
    current = S
    unvisited.remove(S)
    for _ in range(500000):
        for n in unvisited_neighbours(current, unvisited):
            tentative_distance[n] = min(tentative_distance[n], tentative_distance[current] + 1)
        if current in unvisited:
            unvisited.remove(current)
        if E not in unvisited:
            return tentative_distance[E]
        current = min(unvisited, key=lambda x: tentative_distance[x])
    print('Didn"t find it!')
    return None

s = [(x,y) for x in range(num_rows) for y in range(num_cols) if grid[x][y] == 0]
paths = []
for n, S in enumerate(s):
    print(f"{n}/{len(s)}")
    paths.append(get_shortest_path(S))
print(min(paths))