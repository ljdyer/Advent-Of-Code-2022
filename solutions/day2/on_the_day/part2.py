with open('data.txt', 'r') as f:
    data = f.read().splitlines()

letter_to_shape = {
    'A': 'ro',
    'B': 'pa',
    'C': 'sc',
}

letter_to_outcome = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

shape_scores = {'ro': 1, 'pa': 2, 'sc': 3}
me_win = {'ro': 'pa', 'pa': 'sc', 'sc': 'ro'}
me_lose = {'ro': 'sc', 'pa': 'ro', 'sc': 'pa'}


score = 0

for x in data:
    them, me = x.split(' ')
    them = letter_to_shape[them]
    outcome = letter_to_outcome[me]
    if outcome == 'draw':
        score += shape_scores[them]
        score += 3
        print(score)
    elif outcome == 'win':
        score += shape_scores[me_win[them]]
        score += 6
        print(score)
    elif outcome == 'lose':
        score += shape_scores[me_lose[them]]
        print(score)

    

print(score)
    