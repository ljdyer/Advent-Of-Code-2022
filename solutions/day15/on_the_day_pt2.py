import re
from operator import itemgetter

# search_rows = (0, 20)
# search_cols = (0, 20)
# with open('test_data.txt', 'r') as f:
search_rows = (0, 4_000_000)
search_cols = (0, 4_000_000)
with open('data.txt', 'r') as f:
    lines = f.read().splitlines()

sensors = {}
for i, l in enumerate(lines):
    sensors[i] = dict(
        [x for x in zip(
            ['sx', 'sy', 'nx', 'ny'], map(int, re.findall(r'[x|y]=(\-?\d+)', l))
        )]
    )
    


# ====================
def combine_tuples(tuples):

    can_combine = True
    start = 0
    while can_combine and len(tuples) - start > 1:
        t1 = tuples[start]
        t2 = tuples[start+1]
        print(t1, t2)
        s1, f1 = t1
        s2, f2 = t2
        if s1 < f2:
            if f1 >= s2:
                tuples = [(s1, f2)] + tuples[start+2:]
            else:
                pass
        elif s2 < f1:
            if f2 >= s1:
                tuples = [(s2, f1)] + tuples[start+2:]
            else:
                pass
        start += 1
    return tuples

                        
print(combine_tuples([(0,3), (2,7), (8,9), (5,6)]))


    



# ====================
def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)


# ====================
def area_blocked(s, search_rows, search_cols):

    sx, sy, nx, ny = itemgetter('sx', 'sy', 'nx', 'ny')(s)
    dist_s_n = manhattan((sx, sy), (nx, ny))
    blocked = {}
    for r in range(search_rows[0], search_rows[1]+1):
        dist_to_row = abs(sy-r)
        dist_remaining = dist_s_n-dist_to_row
        if dist_remaining >= 0:
            first = sx-dist_remaining
            last = sx + dist_remaining
            blocked[r] = (first, last)
    return blocked
            

# ====================
def tuning_frequency(point):
    y,x = point
    return x*4000000 + y


# for s in sensors.values():
#     print(s)
#     s['blocked']=area_blocked(s, search_rows, search_cols)


# for r in range(search_rows[0], search_rows[1]+1):
#     pass
# can_have_beacon = set()
# ranges = {}
# for row in range(search_rows[0], search_rows[1]+1):
#     print(row)
#     cols_without_beacons = []
#     for sensor in sensors.values():
#         c_without = row_reconnaisance(row, sensor, search_cols)
#         if c_without:
#             cols_without_beacons.append(c_without)
#     ranges[row] = cols_without_beacons
# print('xxx')

# for row, rs in ranges.items():
#     for col in range(search_cols[0], search_cols[1]+1):
#         if any(col >= r[0] and col < r[1] for r in rs):
#             continue
#         else:
#             print(row, col)

