import re

def get_monkeys(real=False):
    if real:
        data_path = '../data.txt'
    else:    
        data_path = '../test_data.txt'
    with open(data_path, 'r') as f:
        data = f.read().splitlines()
    return data

monkeys = get_monkeys(True)
# print(monkeys)

lone_number = [m for m in monkeys if re.match(r"^[a-z]+: \d+$", m)]
lone_number = [m.split(': ') for m in lone_number]
lone_number = {m: int(n) for m, n in lone_number}
# print(lone_number)

waiting = [m for m in monkeys if not re.match(r"^[a-z]+: \d+$", m)]
waiting = [re.findall("([a-z]+): ([a-z]+) (.) ([a-z]+)", m) for m in waiting]
waiting = [list(x[0]) for x in waiting]
# print(waiting)

while waiting:
    next = waiting.pop(0)
    if isinstance(next[1], str):
        if next[1] in lone_number.keys():
            next[1] = lone_number[next[1]]
    if isinstance(next[3], str):
        if next[3] in lone_number.keys():
            next[3] = lone_number[next[3]]
    if isinstance(next[1], int) and isinstance(next[3], int):
        if next[2] == '+':
            lone_number[next[0]] = next[1] + next[3]
        elif next[2] == '-':
            lone_number[next[0]] = next[1] - next[3]
        elif next[2] == '*':
            lone_number[next[0]] = next[1] * next[3]
        elif next[2] == '/':
            lone_number[next[0]] = int(next[1] / next[3])
        else:
            raise ValueError
        if next[0] == 'root':
            print(lone_number[next[0]])
            break
    else:
        waiting.append(next)

# print(lone_number)
    

