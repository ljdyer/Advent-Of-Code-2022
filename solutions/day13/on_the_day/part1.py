import json

with open('../test_data.txt', 'r') as f:
# with open('../data.txt', 'r') as f:
    packet_pairs = f.read().split('\n\n')
    packet_pairs = [pp.split('\n') for pp in packet_pairs]
    packet_pairs = [tuple(json.loads(p) for p in pp) for pp in packet_pairs]


# ====================
def relation(left, right):

    print(f"Compare {left} vs {right}")

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

ordered_pairs = []
for i, pp in enumerate(packet_pairs, start=1):
    print(f"== Pair {i+1} ==")
    left, right = pp
    print(left, right)
    r = relation(left, right)
    if r == 'eq':
        raise ValueError()
    if r == 'lt':
        ordered_pairs.append(i)
    print()

print(ordered_pairs)
print(sum(ordered_pairs))

