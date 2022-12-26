import itertools

def get_data(which: str = 'test'):
    if which == 'real':
        data_path = '../data.txt'
    elif which == 'test2':
        data_path = '../test_data_2.txt'
    else:    
        data_path = '../test_data.txt'
    with open(data_path, 'r') as f:
        data = f.read()
    return data.splitlines()

data = get_data('real')
# print(data)

mapping = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2
}

rev_mapping = {v: k for k, v in mapping.items()}

def snafu_to_dec(this):
    this = [mapping[x] for x in list(this)]
    this = reversed(this)
    sum = 0
    power = 1
    for x in this:
        sum += x*power
        power *= 5
    return sum

for i in data:
    print(snafu_to_dec(i))
print(sum(snafu_to_dec(dec) for dec in data))

def twos(x):
    return sum([2 * 5 ** i for i in range(x)])

def ones(x):
    return sum([5 ** i for i in range(x)])

print(twos(1))
print(twos(2))
print(twos(3))

def add_one(snafu):

    snafu = [mapping[x] for x in list(snafu)]
    if all(x == 2 for x in snafu):
        snafu = [1] + [-2 for _ in range(len(snafu))]
        return ''.join([rev_mapping[x] for x in snafu])
    else:
        for pos in range(1, len(snafu)+1):
            if snafu[-pos] < 2:
                snafu[-pos] += 1
                return ''.join([rev_mapping[x] for x in snafu])
            elif snafu[-pos] == 2:
                # print('XXX', pos)
                snafu[-pos] = -2
                if snafu[-pos-1] < 2:
                    snafu[-pos-1] += 1
                    return ''.join([rev_mapping[x] for x in snafu])
                else:
                    pos += 1

snafu = '2=0--0---11--01=-100'
dec = snafu_to_dec(snafu)
print(dec)
remainder = 30332970236150 - dec
print(remainder)
# while remainder > 0:
#     snafu = add_one(snafu)
#     print(snafu)
#     dec = snafu_to_dec(snafu)
#     print(dec)
    # print(dec, snafu)
#     snafu = add_one(snafu)
# print(snafu)
# def dec_to_snafu(dec):

#     digits = 1
#     twos = 2
#     while twos < dec:
#         digits += 1
#         twos = sum([2 * 5 ** i for i in range(digits)])
#     snafu = [2] + [2 for _ in range(digits-1)]
#     print(dec)
#     print(snafu)
#     current = snafu_to_dec(''.join([rev_mapping[x] for x in snafu]))
#     remainder = dec-current
#     pos = 1
#     while remainder:
#         if snafu[pos] > -2:
#             snafu[pos] -= 1
#             continue
#         elif snafu[pos] == -2:
#             snafu[pos] == 2
#             snafu[pos-1] == 2

        


    # print(snafu_to_dec(snafu))
    # for i in range(len(snafu)):
    #     print(5 ** (len(snafu) - 1 - i))
    # print()
    # return snafu


# print(dec_to_snafu(1))
# print(dec_to_snafu(13))
# print(dec_to_snafu(20))

# print(snafu_to_dec('1=='))




# def dec_to_snafu(this):

#     digits = 1
#     twos = 2
#     while twos < this:
#         digits += 1
#         twos = sum([2 * 5 ** i for i in range(digits)])
#         # print(twos)
#     snafu = [0 for _ in range(digits)]
#     for i in range(1, len(snafu)+1):
#         first_position = 5 ** (len(snafu)-i)
#         next_position = first_position / 5
#         print(first_position, next_position, this)
#         if this >= 2 * first_position:
#             snafu[i-1] += 2
#             this -= (2*first_position)
#         elif this >= first_position + (4 * next_position):
#             snafu[i-1] += 2
#             snafu[i] -= 1
#             this -= (2 * first_position)
#             this += next_position
        
#         elif this >= first_position + (3 * next_position):
#             snafu[i-1] += 2
#             snafu[i] -= 2
#             this -= (2 * first_position)
#             this += (2 * next_position)
#         elif this >= first_position:
#             snafu[i-1] += 1
#             this -= first_position
#         elif this >= first_position - next_position:
#             snafu[i-1] += 1
#             snafu[i] -= 1
#             this -= first_position
#             this += next_position
#         elif this >= first_position - (2 * next_position):
#             snafu[i-1] += 1
#             snafu[i] -= 2
#             this -= first_position
#             this += (2 * next_position)
#         # print(snafu, this)
#     return ''.join([rev_mapping[x] for x in snafu])
#     # return digits, first_position, snafu, this


# dec_test = [1,2,3,4,5,6,7,8,9,10,15,20,2022,12345,314159265]
# for dec in dec_test:
#     print(dec, dec_to_snafu(dec))


# for i in range(1000):

#     print(dec_to_snafu(i))
#     try:
#         assert snafu_to_dec(dec_to_snafu(i)) == i
#     except:
#         print()
#         print(i)
#         print(snafu_to_dec(dec_to_snafu(i)))
#         quit()

# print()
# # print(dec_to_snafu(13))
# print(snafu_to_dec('1=='))