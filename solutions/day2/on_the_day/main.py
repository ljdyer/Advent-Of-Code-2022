with open('data.txt', 'r') as f:
    data = f.read().splitlines()

letter_to_shape = {
    'A': 'ro',
    'B': 'pa',
    'C': 'sc',
    'X': 'ro',
    'Y': 'pa',
    'Z': 'sc'
}

score = 0

for x in data:
    them, me = [letter_to_shape[y] for y in x.split(' ')]
    if me == 'ro':
        score += 1
    elif me == 'pa':
        score += 2
    elif me == 'sc':
        score += 3
    if me == them:
        score += 3
    elif me == 'ro' and them == 'sc':
        score += 6
    elif me == 'sc' and them == 'pa':
        score += 6
    elif me == 'pa' and them == 'ro':
        score += 6

print(score)
    