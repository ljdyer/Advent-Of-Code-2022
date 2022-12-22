def get_data(real=False):
    if real:
        data_path = '../data.txt'
    else:    
        data_path = '../test_data.txt'
    with open(data_path, 'r') as f:
        data = f.read().splitlines()
    return data

# numbers_orig = [int(x) for x in get_data(True)]
numbers_orig = [int(x) for x in get_data()]
numbers_sorted = numbers_orig.copy()
num_numbers = len(numbers_orig)



for i in range(num_numbers):
    number = numbers_orig[i]
    if number != 0:
        start_pos = numbers_sorted.index(number)
        end_pos = (start_pos + number) % (num_numbers)
        numbers_sorted.insert(end_pos, number)
        if start_pos < end_pos:
            del numbers_sorted[numbers_sorted.index(number) + 1]
        else:
            del numbers_sorted[numbers_sorted.index(number)]
        # print(numbers_sorted)
        # print(start_pos)
        # print(number)
        # print(end_pos)
    print(numbers_sorted)
    print()

zero_pos = numbers_sorted.index(0)
one = numbers_sorted[(zero_pos + 1000) % num_numbers]
print(one)
two = numbers_sorted[(zero_pos + 2000) % num_numbers]
print(two)
three = numbers_sorted[(zero_pos + 3000) % num_numbers]
print(three)
print(one + two + three)


# for i in range(len(numbers)):
#     pre_numbers = []
#     while True:
#         x = numbers.pop(0)
#         if isinstance(x, int):
#             break
#         else:
#             pre_numbers.append(x)
#     numbers = numbers + pre_numbers
#     # pos_to_insert = x % num_numbers
#     # numbers.insert(pos_to_insert, f"m{x}")
#     numbers.insert(x, f"m{x}")
    
# pos_0 = numbers.index('m0')
# numbers = numbers[pos_0:] + numbers[:pos_0]

# for i in [0, 6, 12, 18]:
#     x = [0,1,2,3,4,5]
#     x.insert()