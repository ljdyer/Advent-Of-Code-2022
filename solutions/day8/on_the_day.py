# with open('test_data.txt', 'r') as f:
with open('data.txt', 'r') as f:
    rows = f.read().splitlines()    

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


rows = [[int(x) for x in r] for r in rows]
cols = [[r[i] for r in rows] for i in range(len(rows))]

visible = []
# visible from left
for i in range(len(rows)):
    visible_ = [j for j, t in enumerate(rows[i]) if all(t > t_ for t_ in rows[i][:j])]
    visible.extend([(i, j) for j in visible_])
for i in range(len(rows)):
    visible_ = [j for j, t in enumerate(rows[i]) if all(t > t_ for t_ in rows[i][j+1:])]
    visible.extend([(i, j) for j in visible_])
for j in range(len(cols)):
    visible_ = [i for i, t in enumerate(cols[j]) if all(t > t_ for t_ in cols[j][:i])]
    visible.extend([(i, j) for i in visible_])
for j in range(len(cols)):
    visible_ = [i for i, t in enumerate(cols[j]) if all(t > t_ for t_ in cols[j][i+1:])]
    visible.extend([(i, j) for i in visible_])

# for i in range(len(rows)):
#     for j in range(len(rows[i])):
#         if (i,j) in visible:
#             print(f'{bcolors.WARNING}{rows[i][j]}{bcolors.ENDC}', end='')
#         else:
#             print(f'{bcolors.FAIL}{rows[i][j]}{bcolors.ENDC}', end='')
#     print()

# print(len(set(visible)))

def viewing_distance(rows, cols, i, j):
    left = 0
    this = rows[i][j]
    view = list(reversed(rows[i][:j]))
    # print(view)
    for t in view:
        left += 1
        if t >= this:
            break
    # print(left)
    right = 0
    view = rows[i][j+1:]
    # print(view)
    for t in view:
        right += 1
        if t >= this:
            break
    # print(right)
    up = 0
    view = list(reversed(cols[j][:i]))
    # print(view)
    for t in view:
        up += 1
        if t >= this:
            break
    # print(up)
    down = 0
    view = cols[j][i+1:]
    # print(view)
    for t in view:
        down += 1
        if t >= this:
            break
    # print(down)
    return left * right * up * down

scenic_scores = [viewing_distance(rows, cols, i, j) for i in range(len(rows)) for j in range(len(cols))]
print(scenic_scores)
print(max(scenic_scores))