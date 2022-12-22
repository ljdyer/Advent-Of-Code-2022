import re
from operator import itemgetter
from numpy import inf

# with open('test_data.txt', 'r') as f:
with open('data.txt', 'r') as f:
    lines = f.read().splitlines()

sensors = [
    dict(list(zip(
        ['sx', 'sy', 'nx', 'ny'],
        map(int, re.findall(r'[x|y]=(\-?\d+)', l)))))
    for l in lines
]

# ====================
def manhattan(p1, p2):

    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

# ====================
def tuning_frequency(position):

    y,x = position
    return x*4000000 + y

# ====================
def combine_ranges_(ranges):

    for i in range(len(ranges)):
        for j in range(i+1, len(ranges)):
            r1, r2 = sorted([ranges[i], ranges[j]])
            s1, f1 = r1
            s2, f2 = r2
            if s1 <= s2 and f1 >= s2-1:
                del ranges[i]
                del ranges[j-1]
                ranges.append((s1, max(f1, f2)))
                return ranges, True
    return ranges, False

# ====================
def combine_ranges(ranges):

    combined = True
    while combined:
        ranges, combined = combine_ranges_(ranges)
    return ranges
                        
# ====================
def add_to_blocked(s, blocked):

    sx, sy, nx, ny = itemgetter('sx', 'sy', 'nx', 'ny')(s)
    dist_s_n = manhattan((sx, sy), (nx, ny))
    start_row = max(search_rows[0], sy-dist_s_n)
    finish_row = min(search_rows[1], sy+dist_s_n)
    for r in range(start_row, finish_row+1):
        dist_to_row = abs(sy-r)
        dist_remaining = dist_s_n-dist_to_row
        if dist_remaining >= 0:
            first = max(search_cols[0], sx-dist_remaining)
            last = min(search_cols[1], sx+dist_remaining)
            if r not in blocked:
                blocked[r] = [(first, last)]
            else:
                blocked[r] = combine_ranges(blocked[r] + [(first, last)])
    return blocked

# Part 1
blocked = {}
search_row = 2_000_000
search_rows = (search_row, search_row)
search_cols = (-inf, inf)
for s in sensors:
    blocked = add_to_blocked(s, blocked)
num_in_range = sum([f - s for s, f in blocked[search_row]])
num_beacons = len(set([s['nx'] for s in sensors if s['nx'] == search_row]))
print(num_in_range - num_beacons)

# Part 2
blocked = {}
search_rows = (0, 4_000_000)
search_cols = (0, 4_000_000)
for s in sensors:
    blocked = add_to_blocked(s, blocked)
answer = [(row, b) for row, b in blocked.items() if b != [search_cols]]
assert len(answer) == 1
row, blocked = answer[0]
col = [c for c in range(search_cols[0], search_cols[1]) if all(c not in range(s, f+1) for s, f in blocked)]
assert len(col) == 1
print(tuning_frequency((row, col[0])))
