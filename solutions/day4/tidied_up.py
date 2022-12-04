with open('data.txt', 'r') as f:
    lines = f.read().splitlines()

def get_section_ID_lists(line):

    elves = line.split(',')
    elf_ranges = [map(int, elf.split('-')) for elf in elves]
    elf_lists = [list(range(start, finish+1)) for start, finish in elf_ranges]
    return elf_lists

ids = [get_section_ID_lists(l) for l in lines]

# Part 1

def fully_contains(list1, list2):

    if all(x in list2 for x in list1) or all(x in list1 for x in list2):
        return True
    else:
        return False

fully_contained = sum([fully_contains(x[0], x[1]) for x in ids])
print(fully_contained)

# Part 2

def overlap(list1, list2):

    if any(x in list2 for x in list1) or any(x in list1 for x in list2):
        return True
    else:
        return False
    
overlap_ = sum([overlap(x[0], x[1]) for x in ids])
print(overlap_)
