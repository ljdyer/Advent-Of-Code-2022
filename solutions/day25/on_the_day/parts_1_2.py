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

data = get_data('test')
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

# for i in data:
#     print(snafu_to_dec(i))
# print(sum(snafu_to_dec(dec) for dec in data))



def dec_to_snafu(this):

    digits = 1
    twos = 2
    while twos < this:
        digits += 1
        twos = sum([2 * 5 ** i for i in range(digits)])
        # print(twos)
    snafu = [0 for _ in range(digits)]
    for i in range(1, len(snafu)+1):
        first_position = 5 ** (len(snafu)-i)
        next_position = first_position / 5
        if this >= 2 * first_position:
            snafu[i-1] += 2
            this -= (2*first_position)
        elif this >= first_position + (4 * next_position):
            snafu[i-1] += 2
            snafu[i] -= 1
            this -= (2 * first_position)
            this += next_position
        elif this >= first_position + (3 * next_position):
            snafu[i-1] += 2
            snafu[i] -= 2
            this -= (2 * first_position)
            this += (2 * next_position)
        elif this >= first_position:
            snafu[i-1] += 1
            this -= first_position
        elif this >= first_position - next_position:
            snafu[i-1] += 1
            snafu[i] -= 1
            this -= first_position
            this += next_position
        elif this >= first_position - (2 * next_position):
            snafu[i-1] += 1
            snafu[i] -= 2
            this -= first_position
            this += (2 * next_position)
        # print(snafu, this)
    return ''.join([rev_mapping[x] for x in snafu]), this
    # return digits, first_position, snafu, this


dec_test = [1,2,3,4,5,6,7,8,9,10,15,20,2022,12345,314159265]
for dec in dec_test:
    print(dec, dec_to_snafu(dec))

