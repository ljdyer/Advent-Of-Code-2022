import re
import operator
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

# with open('../test_data.txt', 'r') as f:
with open('../data.txt', 'r') as f:
    input = [l.strip() for l in f.read().splitlines()]


def get_ints(string: str):
    return [int(x) for x in re.findall(r'\d+', string)]

# def product(lis: list):
#     product = lis[0]
#     for e in lis[1:]:
#         product *= e
#     return product

monkeys = {}


for line in input:
    if line.startswith('Monkey'):
        monkey_num = get_ints(line)[0]
        monkeys[monkey_num] = {}
        this_monkey = monkeys[monkey_num]
        this_monkey['inspected'] = 0
    elif line.startswith('Starting items:'):
        this_monkey['items'] = get_ints(line)
    elif line.startswith('Operation: new = old'):
        line_split = line.split()
        this_monkey['op'] = ops[line_split[-2]]
        operand = line_split[-1]
        this_monkey['operand'] = int(operand) if operand.isnumeric() else operand
    elif line.startswith('Test: divisible by '):
        this_monkey['test'] = get_ints(line)[0]
    elif line.startswith('If true: throw to'):
        this_monkey[True] = get_ints(line)[0]
    elif line.startswith('If false: throw to'):
        this_monkey[False] = get_ints(line)[0]
    
for round in range(20):
    for monkey_num, monkey in monkeys.items():
        # print(f'Monkey {monkey_num}:')
        items = monkey['items']
        for idx in range(len(items)):
            # print(f'  Monkey inspects an item with a worry level of {items[idx]}.')
            items[idx] = monkey['op'](items[idx], monkey['operand']) if isinstance(monkey['operand'], int) else monkey['op'](items[idx], items[idx])
            items[idx] = items[idx] // 3
            test = items[idx] % monkey['test'] == 0
            throw_to = monkey[test]
            # print(f'    Item with worry level {items[idx]} is thrown to monkey {throw_to}')
            monkeys[throw_to]['items'].append(items[idx])
            monkey['inspected'] += 1
        monkey['items'] = []
    # print(f"After round {round + 1}:")
    # for monkey_num, monkey in monkeys.items():
    #     print(f"Monkey {monkey_num}: {monkey['items']}")
    # print()

inspected_nums = [v['inspected'] for v in monkeys.values()]
for monkey, inspected in enumerate(inspected_nums):
    print(f"Monkey {monkey} inspected items {inspected} times.")
top_two = list(sorted(inspected_nums))[-2:]
one, two = top_two
print(one * two)

