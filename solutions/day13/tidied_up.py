import json

with open('data.txt', 'r') as f:
    data = f.read()

# ====================
def relation(l, r):

    # Both values are integers
    if isinstance(l, int) and isinstance(r, int):
        return [x[0] for x in [('lt', l<r), ('eq',l==r), ('gt', l>r)] if x[1]][0]
    # Exactly one value is an integer
    l = [l] if isinstance(l, int) else l.copy()
    r = [r] if isinstance(r, int) else r.copy()
    while l and r:
        rel = relation(l.pop(0), r.pop(0))
        if rel != 'eq':
            return rel
    return [x[0] for x in [('eq', not l and not r), ('lt', not l), ('gt', True)] if x[1]][0]
    

# Part 1
packet_pairs = [pp.split('\n') for pp in data.split('\n\n')]
packet_pairs = [[json.loads(p) for p in pp] for pp in packet_pairs]
ordered_pairs = [i for i, pp in enumerate(packet_pairs, start=1) if relation(pp[0], pp[1]) == 'lt']
print(sum(ordered_pairs))

# Part 2
packets = [p for pp in packet_pairs for p in pp]
less_than_6 = [p for p in packets if relation(p, [[6]]) == 'lt']
less_than_2 = [p for p in packets if relation(p, [[2]]) == 'lt']
print((len(less_than_2) + 1) * (len(less_than_6) + 2))