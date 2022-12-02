with open('data.txt', 'r') as f:
    letter_pairs = [line.split() for line in f.read().splitlines()]

# === PART 1 ===
LETTER_SHAPE = {'A': 'ro', 'B': 'pa', 'C': 'sc', 'X': 'ro', 'Y': 'pa', 'Z': 'sc'}
SHAPE_ORDER = ['pa', 'ro', 'sc']
ME_OPPONENT_OUTCOME = {
    shape: dict(zip(SHAPE_ORDER[i:] + SHAPE_ORDER[:i], ['draw', 'win', 'lose']))
    for i, shape in enumerate(SHAPE_ORDER)
}
SHAPE_SCORES = {'ro': 1, 'pa': 2, 'sc': 3}
OUTCOME_SCORES = {'win': 6, 'draw': 3, 'lose': 0}

shape_pairs = [(LETTER_SHAPE[opponent], LETTER_SHAPE[me]) for opponent, me in letter_pairs]
score = sum([
    SHAPE_SCORES[me] + OUTCOME_SCORES[ME_OPPONENT_OUTCOME[me][opponent]]
    for opponent, me in shape_pairs]
)
print(score)

# === PART 2 ===
LETTER_OUTCOME = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
OPPONENT_OUTCOME_ME = {
    shape: dict(zip(['draw', 'lose', 'win'], SHAPE_ORDER[i:] + SHAPE_ORDER[:i]))
    for i, shape in enumerate(SHAPE_ORDER)
}

shape_outcome_pairs = [(LETTER_SHAPE[opponent], LETTER_OUTCOME[outcome]) for opponent, outcome in letter_pairs]
score = sum([
    SHAPE_SCORES[OPPONENT_OUTCOME_ME[opponent][outcome]] + OUTCOME_SCORES[outcome]
    for opponent, outcome in shape_outcome_pairs
])
print(score)
