with open('data.txt', 'r') as f:
    lines = f.read().splitlines()

def get_section_ID_lists(line):
    elves = line.split(',')
    elf_ranges = [map(int, elf.split('-')) for elf in elves]
    elf_lists = [list(range(start, finish+1)) for start, finish in elf_ranges]
    return elf_lists

ids = [get_section_ID_lists(l) for l in lines]

# Part 1
print(sum([all(z in x[0] for z in x[1]) or all(z in x[1] for z in x[0]) for x in ids]))

# Part 2
print(sum([any(z in x[0] for z in x[1]) or any(z in x[1] for z in x[0]) for x in ids]))