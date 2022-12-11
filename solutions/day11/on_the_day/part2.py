import re
import operator
from datetime import datetime
from collections import Counter

# with open('../test_data.txt', 'r') as f:
with open('../data.txt', 'r') as f:
    input = [l.strip() for l in f.read().splitlines()]

def get_ints(string: str):
    return [int(x) for x in re.findall(r'\d+', string)]

class Item:
    def __init__(self, num, tests):
        self.remainder = {t: num % t for t in tests}

    def add(self, x):
        self.remainder = {t: (r+x) % t for t, r in self.remainder.items()}

    def mul(self, x):
        self.remainder = {t: (r*x) % t for t, r in self.remainder.items()}
    
    def sq(self):
        self.remainder = {t: (r**2) % t for t, r in self.remainder.items()}


monkeys = {}

for line in input:
    if line.startswith('Monkey'):
        monkey_num = get_ints(line)[0]
        monkeys[monkey_num] = {}
        this_monkey = monkeys[monkey_num]
        this_monkey['inspected'] = 0
    elif line.startswith('Starting items:'):
        this_monkey['items'] = [x for x in get_ints(line)]
    elif line.startswith('Operation: new = old'):
        line_split = line.split()
        op = line_split[-2]
        operand = line_split[-1]
        if operand == 'old':

            if op == '*':
                op = 'sq'
                operand = 0
            else:
                raise ValueError('!!!')
        this_monkey['op'] = op
        this_monkey['operand'] = int(operand)
    elif line.startswith('Test: divisible by '):
        this_monkey['test'] = get_ints(line)[0]
    elif line.startswith('If true: throw to'):
        this_monkey[True] = get_ints(line)[0]
    elif line.startswith('If false: throw to'):
        this_monkey[False] = get_ints(line)[0]
    elif line == '':
        pass
    else:
        raise ValueError('!!!')

print(monkeys)
tests = [monkey['test'] for monkey in monkeys.values()]
print(tests)
for monkey in monkeys.values():
    monkey['items'] = list(map(lambda x: Item(x, tests), monkey['items']))


start_time = datetime.now()
for round in range(10_000):
    for monkey_num, monkey in monkeys.items():
        items = monkey['items']
        op = monkey['op']
        operand = monkey['operand']
        for item in items:
            if op == '+':
                item.add(operand)
            elif op == '*':
                item.mul(operand)
            elif op == 'sq':
                item.sq()
            test = bool(item.remainder[monkey['test']] == 0)
            throw_to = monkey[test]
            monkeys[throw_to]['items'].append(item)
            monkey['inspected'] += 1
        monkey['items'] = []
end_time = datetime.now()
print(f"Time taken: {end_time-start_time}")

inspected_nums = [v['inspected'] for v in monkeys.values()]
for monkey, inspected in enumerate(inspected_nums):
    print(f"Monkey {monkey} inspected items {inspected} times.")
top_two = list(sorted(inspected_nums))[-2:]
# print(monkeys[0])
one, two = top_two
print(one * two)
