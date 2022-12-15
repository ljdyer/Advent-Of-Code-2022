import re
from operator import itemgetter

# search_rows = (0, 20)
# search_cols = (0, 20)
# with open('../test_data.txt', 'r') as f:
search_rows = (0, 4_000_000)
search_cols = (0, 4_000_000)
with open('../data.txt', 'r') as f:
    lines = f.read().splitlines()

sensors = {}
for i, l in enumerate(lines):
    sensors[i] = dict(
        [x for x in zip(
            ['sx', 'sy', 'nx', 'ny'], map(int, re.findall(r'[x|y]=(\-?\d+)', l))
        )]
    )
    
# ====================
def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

# ====================
def tuning_frequency(point):
    y,x = point
    return x*4000000 + y


# ====================
def combine_tuples_(tuples):

    for i in range(len(tuples)):
        for j in range(1, len(tuples)):
            if i != j:
                s1, f1 = tuples[i]
                s2, f2 = tuples[j]
                if s1 <= s2:
                    if f1 < s2-1:
                        pass
                    elif f1 >= s2-1:
                        del tuples[i]
                        del tuples[j-1]
                        tuples.append((s1, max(f1, f2)))
                        return tuples, True
                elif s2 <= s1:
                    if f2 < s1-1:
                        pass
                    elif f2 >= s1-1:
                        del tuples[i]
                        del tuples[j-1]
                        tuples.append((s2, max(f1, f2)))
                        return tuples, True
    return tuples, False

# ====================
def combine_tuples(tuples):

    combined = True
    while combined:
        tuples, combined = combine_tuples_(tuples)
    return tuples
                        
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
                blocked[r] = combine_tuples(blocked[r] + [(first, last)])
    return blocked
    
blocked = {}
for s in sensors.values():
    print(s)
    blocked = add_to_blocked(s, blocked)


answer = [(row, b) for row, b in blocked.items() if b != [search_cols]]
print(answer)
assert len(answer) == 1
row, blocked = answer[0]
print(row)
col = [c for c in range(search_cols[0], search_cols[1]) if all(c not in range(s, f+1) for s, f in blocked)]
assert len(col) == 1
print(col[0])
print(tuning_frequency((row, col[0])))
            






