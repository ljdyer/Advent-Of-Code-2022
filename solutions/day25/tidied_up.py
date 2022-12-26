mapping = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
rev_mapping = {v: k for k, v in mapping.items()}

# ====================
def snafu_to_dec(snafu: str) -> int:
    """Convert from snafu to decimal"""

    snafu = [mapping[x] for x in list(snafu)]
    return sum(x * 5 ** power for power, x in enumerate(reversed(snafu)))


# ====================
def add_one(snafu: str) -> str:
    """Add one to a snafu number"""

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
                snafu[-pos] = -2
                if snafu[-pos-1] < 2:
                    snafu[-pos-1] += 1
                    return ''.join([rev_mapping[x] for x in snafu])
                else:
                    pos += 1


# ====================
def add(power: int, snafu: str) -> str:
    """Add a power of 5 to a snafu number
    (e.g. if power=3, add 125 to snafu)"""

    if power == 0:
        return add_one(snafu)
    else:
        head = snafu[:-power]
        tail = snafu[-power:]
        head = add_one(head)
        return head + tail


# ====================
def next_power(num: int) -> int:
    """Get the highest integer x such that 5**x <= num"""

    power = 0
    while 5 ** power <= num:
        power += 1
    return power - 1


# ====================
def snafu_len(dec):
    """Get the number of characters in the snafu
    representation of dec"""

    x = 1
    while True:
        if sum([2 * 5 ** i for i in range(x)]) < dec:
            x += 1
        else:
            return x


# ====================
def dec_to_snafu(dec):
    """Convert from decimal to snafu"""
    
    len = snafu_len(dec)
    snafu = '1'.zfill(len)
    current = 1
    while current != dec:
        remainder = dec - current
        power = next_power(remainder)
        snafu = (add(power, snafu))
        current = snafu_to_dec(snafu)
    return snafu


# Check against examples
with open('examples.txt', 'r') as f:
    examples = f.read().splitlines()[1:]
examples = [l.split() for l in examples]
for dec, snafu in examples:
    assert dec_to_snafu(int(dec)) == snafu
    assert snafu_to_dec(snafu) == int(dec)

# Run test
with open('test_data.txt', 'r') as f:
    test = f.read().splitlines()
answer_dec = sum(snafu_to_dec(s) for s in test)
answer_snafu = dec_to_snafu(answer_dec)
assert answer_snafu == '2=-1=0'

# Get answer
with open('data.txt', 'r') as f:
    test = f.read().splitlines()
answer_dec = sum(snafu_to_dec(s) for s in test)
answer_snafu = dec_to_snafu(answer_dec)
print(answer_snafu)
