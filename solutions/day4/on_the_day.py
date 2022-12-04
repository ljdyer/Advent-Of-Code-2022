# with open('test_data.txt', 'r') as f:
with open('data.txt', 'r') as f:
    lines = f.read().splitlines()

pairs = [l.split(',') for l in lines]
ids = [[list(range(int(p.split('-')[0]), int(p.split('-')[1]) + 1)) for p in pair] for pair in pairs]

def fully_contains(list1, list2):

    if all(x in list2 for x in list1):
        return True
    elif all(x in list1 for x in list2):
        return True
    else:
        return False

fully_contained = sum([fully_contains(x[0], x[1]) for x in ids])
print(fully_contained)


# Part 2
def overlap(list1, list2):

    if any(x in list2 for x in list1):
        return True
    elif any(x in list1 for x in list2):
        return True
    else:
        return False
    
overlap_ = sum([overlap(x[0], x[1]) for x in ids])
print(overlap_)
