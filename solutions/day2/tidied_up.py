with open('data.txt', 'r') as f:
    data = f.read().splitlines()

letter_to_shape = {
    'A': 'ro', 'B': 'pa', 'C': 'sc',
    'X': 'ro', 'Y': 'pa', 'Z': 'sc'
}
shape_scores = {'ro': 1, 'pa': 2, 'sc': 3}
shape_precedence = ['ro', 'sc', 'pa', 'ro']

# Part 1
score = 0
for x in data:
    them, me = [letter_to_shape[y] for y in x.split(' ')]
    score += shape_scores[me]
    if them == me:
        score += 3
    elif shape_precedence[shape_precedence.index(me) + 1] == them:
        score += 6
print(score)

# Part 2
letter_to_outcome = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
precedence_reverse = list(reversed(shape_precedence))
score = 0
for x in data:
    them, outcome = x.split(' ')
    them = letter_to_shape[them]
    outcome = letter_to_outcome[outcome]
    if outcome == 'draw':
        score += 3
        score += shape_scores[them]
    elif outcome == 'win':
        score += 6
        score += shape_scores[precedence_reverse[precedence_reverse.index(them) + 1]]
    elif outcome == 'lose':
        score += shape_scores[shape_precedence[shape_precedence.index(them) + 1]]
print(score)