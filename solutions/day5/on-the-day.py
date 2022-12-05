import re
from time import sleep
from os import system

PRINT=True

# with open('test_data.txt', 'r') as f:
#     lines = f.read().splitlines()
# raw_lines, raw_instructions = lines[:3], lines[5:]
with open('data.txt', 'r') as f:
    lines = f.read().splitlines()
raw_lines, raw_instructions = lines[:8], lines[10:]

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
    find = find[0]
    return(int(find[0]), int(find[1])-1, int(find[2])-1)

def crate_display(crate):
    if crate is None:
        return '   '
    else:
        return f'[{crate}]'

def print_rows(rows):
    row_display = [' '.join([crate_display(c) for c in r]) for r in rows]
    print('\n'.join(row_display))
        
        
rows = [get_crates(l) for l in raw_lines]
instructions = [parse_instruction(i) for i in raw_instructions]

# Part 1
# if PRINT:
#     print_rows(rows)
# for inst in instructions:
#     num, from_col, to_col = inst
#     for _ in range(num):
#         from_row = next((i for i in range(len(rows)) if rows[i][from_col] is not None))
#         to_row = next(
#             (i-1 for i in range(len(rows)) if rows[i][to_col] is not None),
#             len(rows) - 1
#         )
#         if to_row < 0:
#             rows = [[None for t in range(len(rows[0]))]] + rows
#             from_row += 1
#             to_row = 0
#         # Move the crate
#         z = rows[from_row][from_col]
#         rows[from_row][from_col] = None
#         rows[to_row][to_col] = z
#         if PRINT:
#             print('=========================')
#             print(f'From: {from_row}, {from_col}')
#             print(f'To: {to_row}, {to_col}')
#             print_rows(rows)

# Part 2            
if PRINT:
    print_rows(rows)
for inst in instructions:
    num, from_col, to_col = inst
    from_start_row = next((i for i in range(len(rows)) if rows[i][from_col] is not None))
    to_stop_row = next(
        (i for i in range(len(rows)) if rows[i][to_col] is not None),
        len(rows)
    )
    from_stop_row = from_start_row + num
    to_start_row = to_stop_row - num
    if to_start_row < 0:
        for __ in range(-to_start_row):
            rows = [[None for t in range(len(rows[0]))]] + rows.copy()
            from_start_row += 1
            from_stop_row += 1
            to_start_row += 1
            to_stop_row += 1
    if PRINT:
        print(f'From: {from_start_row}-{from_stop_row}, {from_col}')
        print(f'To: {to_start_row}-{to_stop_row}, {to_col}')
    # Move the crates
    crates = [[c for c in rows[k][from_col]] for k in range(from_start_row, from_stop_row)]
    crates = [c[0] for c in crates]
    print(crates)
    for k in range(from_start_row, from_stop_row):
        rows[k][from_col] = None
    for r, crate in zip(list(range(to_start_row, to_stop_row)), crates):
        print(crate)
        rows[r][to_col] = crate
    if PRINT:
        print('=========================')
        print_rows(rows)
        print('=========================')


letters = []
for i in range(len(rows[0])):
    letters.append(next(rows[j][i] for j in range(len(rows)) if rows[j][i] is not None))
print()
print(''.join(letters))

    
    
    