import json

with open('data.txt', 'r') as f:
    data = f.read()


# ====================
def relation(left, right):

    # Both values are integers
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 'lt'
        elif left == right:
            return 'eq'
        else:
            return 'gt'
    # Exactly one value is an integer
    elif isinstance(left, int):
        left, right = [left], right.copy()
    elif isinstance(right, int):
        left, right = left.copy(), [right]
    # Both values are lists
    else:
        left, right = left.copy(), right.copy()
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

# Part 1
packet_pairs = [pp.split('\n') for pp in data.split('\n\n')]
packet_pairs = [[json.loads(p) for p in pp] for pp in packet_pairs]
ordered_pairs = [i for i, pp in enumerate(packet_pairs, start=1) if relation(pp[0], pp[1]) == 'lt']
print(sum(ordered_pairs))

# Part 2
packets = [p for pp in packet_pairs for p in pp]
less_than_2, between_2_and_6 = (0, 0)
for p in packets:
    if relation(p, [[2]]) == 'lt':
        less_than_2 += 1
    elif relation(p, [[6]]) == 'lt':
        between_2_and_6 += 1
pos_2 = less_than_2 + 1
pos_6 = pos_2 + between_2_and_6 + 1
print(pos_2 * pos_6)

