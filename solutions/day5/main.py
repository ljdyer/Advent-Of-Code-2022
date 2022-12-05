import re
from time import sleep
from os import system

# with open('test_data.txt', 'r') as f:
#     lines = f.read().splitlines()
# raw_lines = lines[:3]
# raw_instructions = lines[5:]
with open('data.txt', 'r') as f:
    lines = f.read().splitlines()
raw_lines = lines[:8]
raw_instructions = lines[10:]

def get_crates(line):
    line = line.replace('    ', '[ ]')
    find = re.findall(r'\[.\]', line)
    return [get_letter(f) for f in find]

def get_letter(crate):

    letters = [x for x in crate if x.isalpha()]
    if len(letters) > 0:
        return letters[0]
    else:
        return None

def parse_instruction(inst):
    find = re.findall(r'move (.*) from (.*) to (.*)', inst)

    return tuple([int(f) for f in find[0]])



rows = [get_crates(l) for l in raw_lines]
instructions = [parse_instruction(i) for i in raw_instructions]

for r in rows:
    print(r)
for inst in instructions:
    num, from_, to = inst
    from_ = from_ - 1
    to = to - 1
    for count in range(num):
        # system('cls')
        print('=========================')
        # FROM
        for i in range(len(rows)):
            if rows[i][from_] is None:
                continue
            else:
                from_row = i
                break
        # TO
        to_row = len(rows) - 1
        for i in range(len(rows)):
            if rows[i][to] is None:
                continue
            else:
                print(f"XXX: {rows[i][to]}")
                to_row = i-1
                break

        print(to_row)
        if to_row < 0:
            print('adding row')
            rows = [[None for t in range(len(rows[0]))]] + rows.copy()
            from_row += 1
            print(len(rows))
            to_row = 0
        print(f'From: {from_row}, {from_}')
        print(f'To: {to_row}, {to}')
        z = rows[from_row][from_]
        rows[from_row][from_] = None
        rows[to_row][to] = z
        for r in rows:
            print(r)


letters = []
for i in range(len(rows[0])):
    letters.append(next(rows[j][i] for j in range(len(rows)) if rows[j][i] is not None))
print()
print(''.join(letters))

    
    
    