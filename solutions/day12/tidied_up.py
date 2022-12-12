import string
from numpy import inf
order = {letter: number for number, letter in enumerate(string.ascii_lowercase)}

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
all_nodes = {(x, y) for x in range(num_rows) for y in range(num_cols)}

# Convert letters to elevations
grid = [[order[x] for x in r] for r in grid]

# ====================
def elevation(point):
    x, y = point
    try:
        return grid[x][y]
    except:
        return inf

# ====================
def neighbours(point: tuple) -> list:
    x,y = point
    return [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

# ====================
def unvisited_neighbours(current_point, unvisited):
    return [n for n in neighbours(current_point)
        if elevation(n) < elevation(current_point) + 2 and n in unvisited]
    
# ====================
def get_shortest_path(S: tuple, max_steps: int=5000000) -> int:
    unvisited = all_nodes.copy()
    tentative_distance = {node: inf for node in unvisited}
    tentative_distance[S] = 0
    current = S
    unvisited.remove(S)
    for _ in range(max_steps):
        for n in unvisited_neighbours(current, unvisited):
            tentative_distance[n] = min(tentative_distance[n], tentative_distance[current] + 1)
        if current in unvisited:
            unvisited.remove(current)
        if E not in unvisited:
            return tentative_distance[E]
        current = min(unvisited, key=lambda x: tentative_distance[x])
    print("Didn't find sortest path in {max_steps} steps. Consider increasing value of max_steps.")
    return None

# Part 1
print(get_shortest_path(S))

# Part 2
def is_edge_a(node):
    """Return false if point is not an 'a' or if it is an 'a' surrounded by other 'a's"""
    if elevation(node) != 0:
        return False
    elif all([elevation(n) == 0 for n in neighbours(node)]):
        return False
    else:
        return True

candidates = [n for n in all_nodes if is_edge_a(n)]
print(len(candidates))
paths = []
for n, S in enumerate(candidates):
    print(f"{n}/{len(candidates)}")
    paths.append(get_shortest_path(S))
print(min(paths))