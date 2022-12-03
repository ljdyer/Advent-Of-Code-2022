import string

# with open('test_data.txt', 'r') as f:
with open('data.txt', 'r') as f:
    lines = f.read().splitlines()

for l in lines:
    print(len(l)/2)
halved = [(l[:int(len(l)/2)], l[int(len(l)/2):]) for l in lines]
shared_letter = [[x for x in h[0] if x in h[1]][0] 
                 for h in halved]
LETTER_PRIORITY = {l: p for (l, p) in
                   list(zip(string.ascii_lowercase, list(range(1, 27)))) + \
                   list(zip(string.ascii_uppercase,list(range(27, 53))))}
print(sum([LETTER_PRIORITY[l] for l in shared_letter]))

# Part 2
groups_of_three = [lines[i:i+3] for i in range(0, len(lines), 3)]
shared_letter = [[x for x in h[0] if x in h[1] and x in h[2]][0]
                 for h in groups_of_three]
print(sum([LETTER_PRIORITY[l] for l in shared_letter]))
