import re
from operator import itemgetter

# with open('../test_data.txt', 'r') as f:
with open('../data.txt', 'r') as f:
    lines = f.read().splitlines()

sensors = {}
for i, l in enumerate(lines):
    sensors[i] = dict(
        [x for x in zip(
            ['sx', 'sy', 'nx', 'ny'], map(int, re.findall(r'[x|y]=(\-?\d+)', l))
        )]
    )
    

def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def row_reconnaisance(row: int, s: dict):

    print(s)
    sx, sy, nx, ny = itemgetter('sx', 'sy', 'nx', 'ny')(s)
    dist_s_n = manhattan((sx, sy), (nx, ny))
    dist_to_row = abs(row - sy)
    remaining_dist = dist_s_n - dist_to_row
    if remaining_dist >= 0:
        cols_without_beacons = list(range(min(sx-remaining_dist, sx+remaining_dist), max(sx-remaining_dist, sx+remaining_dist)+1))
    else:
        cols_without_beacons = []
    if ny == row:
        cols_with_beacons = [nx]
        # print(cols_with_beacons)
    else:
        cols_with_beacons = []
    return cols_with_beacons, cols_without_beacons


ROW_NUM = 2_000_000
cols_with_beacons = []
cols_without_beacons = []
for sensor in sensors.values():
    c_with, c_without = row_reconnaisance(ROW_NUM, sensor)
    cols_with_beacons.extend(c_with)
    cols_without_beacons.extend(c_without)
cols_without_beacons = set(cols_without_beacons)
cols_with_beacons = set(cols_with_beacons)
cols_without_final = sorted(cols_without_beacons.difference(cols_with_beacons))
# print(cols_without_final)
print(len(cols_without_final))