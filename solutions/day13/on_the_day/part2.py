import json

# with open('../test_data.txt', 'r') as f:
with open('../data.txt', 'r') as f:
    packets = [l for l in f.read().splitlines() if len(l) > 0]

packets = [json.loads(p) for p in packets]
print(len(packets))

# ====================
def relation(left, right):

    # print(f"Compare {left} vs {right}")

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 'lt'
        elif left == right:
            return 'eq'
        else:
            return 'gt'
    elif isinstance(left, int):
        left = [left]
        right = right.copy()
    elif isinstance(right, int):
        left = left.copy()
        right = [right]
    else:
        left = left.copy()
        right = right.copy()

    while left and right:
        r = relation(left.pop(0), right.pop(0))
        if r == 'eq':
            continue
        else:
            return r
    if not left and not right:
        return 'eq'
    elif not left:
        return 'lt'
    else:
        return 'gt'



less_than_2 = []
between_2_and_6 = []
greater_than_6 = []

for p in packets:
    r_2 = relation(p, [[2]])
    if r_2 == 'lt':
        less_than_2.append(p)
    else:
        r_6 = relation(p, [[6]])
        if r_6 == 'lt':
            between_2_and_6.append(p)
        elif r_6 == 'gt':
            greater_than_6.append(p)
        else:
            raise ValueError()

pos_2 = len(less_than_2) + 1
pos_6 = pos_2 + len(between_2_and_6) + 1
print(pos_2, pos_6)
print(pos_2 * pos_6)
        
    
    
