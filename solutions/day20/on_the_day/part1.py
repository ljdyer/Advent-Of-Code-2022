def get_data(real=False):
    if real:
        data_path = '../data.txt'
    else:    
        data_path = '../test_data.txt'
    with open(data_path, 'r') as f:
        data = f.read().splitlines()
    return data

letters = 'abcdefghijklmnopqrs'
# numbers_orig = ([int(x) for x in get_data()])
numbers_orig = ([int(x) for x in get_data(True)])
numbers_marked = []
for i in range(len(numbers_orig)):
    numbers_marked.append(f"{numbers_orig[i]}{letters[numbers_orig[:i].count(numbers_orig[i])]}")
print(numbers_marked)
numbers_sorted = numbers_marked.copy()
for num in numbers_marked:
    cur_idx = numbers_sorted.index(num)
    del numbers_sorted[cur_idx]
    new_idx = (cur_idx + int(num[:-1])) % len(numbers_sorted)
    numbers_sorted.insert(new_idx, num)
    # print(numbers_sorted)

thousandth = numbers_sorted[(numbers_sorted.index('0a') + 1000) % len(numbers_sorted)]
two_thousandth = numbers_sorted[(numbers_sorted.index('0a') + 2000) % len(numbers_sorted)]
three_thousandth = numbers_sorted[(numbers_sorted.index('0a') + 3000) % len(numbers_sorted)]
print(int(thousandth[:-1]) + int(two_thousandth[:-1]) + int(three_thousandth[:-1]))