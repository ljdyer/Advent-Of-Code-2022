import re

def get_monkeys(real=True):
    if real:
        data_path = '../data.txt'
    else:    
        data_path = '../test_data.txt'
    with open(data_path, 'r') as f:
        data = f.read().splitlines()
    return data

def rearrange(l, r):
    if re.match(r'[a-z]+', l):
        if x := re.findall(r'([a-z]+) (.) (\d+)', r):
            var, sign, num = x[0]
            if sign == '+':
                return f"({l}) - {num}", var
            elif sign == '-':
                return f"({l}) + {num}", var
            elif sign == '*':
                return f"({l}) / {num}", var
            elif sign == '/':
                return f"({l}) * {num}", var
            else:
                raise ValueError
        elif x := re.findall(r'(\d+)+ (.) ([a-z]+)', r):
            num, sign, var = x[0]
            if sign == '+':
                return f"({l}) - {num}", var
            elif sign == '-':
                return f"{num} - ({l})", var
            elif sign == '*':
                return f"({l}) / {num}", var
            elif sign == '/':
                return f"{num} / {l}", var
            else:
                raise ValueError
        else:
            raise ValueError
    else:
        raise ValueError
        


monkeys = get_monkeys()
monkeys = [m.split(': ') for m in monkeys]
# print(monkeys)

number = {m: int(n) for m, n in monkeys if n.isnumeric()}
del number['humn']
waiting = {m: n for m, n in monkeys if not n.isnumeric()}
root = waiting['root']
del waiting['root']

while True:
    new_waiting = {}
    for w in waiting.keys():
        new = waiting[w]
        for m, n in number.items():
            new = new.replace(m, str(n))
        new_waiting[w] = new
        try:
            number[w] = int(eval(waiting[w]))
            del new_waiting[w]
        except:
            pass
    if waiting == new_waiting:
        break
    else:
        waiting = new_waiting
print(waiting)
print(number)

# print(waiting)
# print(number)
root_l, root_r = root.split(' + ')
print(root_l)
print(root_r)

humn = [(w, v) for w, v in waiting.items() if 'humn' in v]
assert len(humn) == 1

print()
humn = humn[0]
l, r = humn
humn = rearrange(l, r)[0]
del waiting[l]
print(humn)

while True:
    to_substitute = re.findall(r'[a-z]+', humn)
    assert(len(to_substitute)) == 1
    eqn_ = [(w, v) for w, v in waiting.items() if to_substitute[0] in v]
    if len(eqn_) == 1:
        l, r = eqn_[0]
        try:
            eqn_l, eqn_r = rearrange(l, r)
        except:
            break
        humn = humn.replace(eqn_r, eqn_l)
        del waiting[l]
        print(humn)
    elif len(eqn_) == 0:
        break
    else:
        raise ValueError


root_l, root_r = root.split(' + ')
if root_l in number.keys():
    root_l = number[root_l]
if root_r in number.keys():
    root_r = number[root_r]
if root_r in waiting.keys():
    root_l = waiting[root_l]
    del waiting[root_l]
if root_r in waiting.keys():
    root_r_ = waiting[root_r]
    del waiting[root_r]
    root_r = root_r_
print()
print(root_l)
print(root_r)

print(f"{root_l} == {root_r}")
print(f"humn == {humn}")
print()
humn = humn.replace(root_l, str(root_r))
print(eval(humn))