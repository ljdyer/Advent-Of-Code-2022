def get_data(real=False):
    if real:
        data_path = '../data.txt'
    else:    
        data_path = '../test_data.txt'
    with open(data_path, 'r') as f:
        data = f.read().splitlines()
    return data

letters = 'abcdefghijklmnopqrs'

def mix_numbers(numbers, n=10):
    
    numbers_marked = []
    for i in range(len(numbers)):
        numbers_marked.append(f"{numbers[i]}{letters[numbers[:i].count(numbers[i])]}")
    numbers_sorted = numbers_marked.copy()
    for _ in range(n):
        for num in numbers_marked:
            cur_idx = numbers_sorted.index(num)
            del numbers_sorted[cur_idx]
            new_idx = (cur_idx + int(num[:-1])) % len(numbers_sorted)
            numbers_sorted.insert(new_idx, num)
    return [int(n[:-1]) for n in numbers_sorted]


# numbers = ([int(x) for x in get_data()])
numbers = ([int(x) for x in get_data(True)])

numbers = [n * 811589153 for n in numbers]
# numbers_sorted = numbers.copy()
# for _ in range(10):
numbers_sorted = mix_numbers(numbers)
    # print(numbers_sorted)
thousandth = numbers_sorted[(numbers_sorted.index(0) + 1000) % len(numbers_sorted)]
two_thousandth = numbers_sorted[(numbers_sorted.index(0) + 2000) % len(numbers_sorted)]
three_thousandth = numbers_sorted[(numbers_sorted.index(0) + 3000) % len(numbers_sorted)]
print(thousandth + two_thousandth + three_thousandth)