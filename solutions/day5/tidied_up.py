import itertools
import os
import re
from time import sleep

ROWS_TO_DISPLAY = 50

# with open('test_data.txt', 'r') as f:
#     lines = f.read().splitlines()
# raw_lines, raw_instructions = lines[:3], lines[5:]
with open('data.txt', 'r') as f:
    lines = f.read().splitlines()
raw_lines, raw_instructions = lines[:8], lines[10:]

def get_crates(line):
    line = line.replace('    ', '[ ]')
    crates = re.findall(r'\[.\]', line)
    return [next((x for x in c if x.isalpha()), None) for c in crates]

def parse_instruction(inst):
    find = re.findall(r'move (.*) from (.*) to (.*)', inst)[0]
    return(int(find[0]), int(find[1])-1, int(find[2])-1)

def transpose(lis: list):
    return list(map(list, itertools.zip_longest(*lis, fillvalue=None)))

def print_stacks(stacks):
    num_rows = ROWS_TO_DISPLAY
    # num_rows = max(map(len, stacks))
    stacks_filled = [([' '] * (num_rows-len(stack))) + stack for stack in stacks]
    rows = transpose(stacks_filled)
    row_display = [' '.join([('   ' if c == ' ' else f'[{c}]') for c in r]) for r in rows]
    print('\n'.join(row_display))

def get_top_letters(stacks):
    top_letters = [s[0] for s in stacks]
    return ''.join(top_letters)
        
def part1(stacks, instructions):
    os.system('cls')
    print_stacks(stacks)
    print()
    sleep(0.1)
    for inst in instructions:
        num, from_stack, to_stack = inst
        for _ in range(num):
            crate = stacks[from_stack].pop(0)
            stacks[to_stack].insert(0, crate)
        os.system('cls')
        print_stacks(stacks)
        print()
        sleep(0.1)
    print(get_top_letters(stacks))

def part2(stacks, instructions):
    os.system('cls')
    print_stacks(stacks)
    print()
    sleep(0.1)
    for inst in instructions:
        num, from_stack, to_stack = inst
        crates = stacks[from_stack][:num]
        stacks[from_stack] = stacks[from_stack][num:]
        stacks[to_stack] = crates + stacks[to_stack]
        os.system('cls')
        print_stacks(stacks)
        print()
        sleep(0.1)
    print(get_top_letters(stacks))


# ====================
if __name__ == "__main__":

    rows = [get_crates(l) for l in raw_lines]
    rows_transposed = transpose(rows)
    stacks = [[x for x in l if x is not None] for l in rows_transposed]
    instructions = [parse_instruction(i) for i in raw_instructions]

    # part1(stacks, instructions)
    part2(stacks, instructions)

    
    
    