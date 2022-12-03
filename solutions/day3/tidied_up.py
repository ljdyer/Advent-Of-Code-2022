import string

with open('data.txt', 'r') as f:
    lines = f.read().splitlines()

# Part 1
halved = [(l[:int(len(l)/2)], l[int(len(l)/2):]) for l in lines]
shared_letter = [[x for x in h[0] if x in h[1]][0] 
                 for h in halved]
LETTER_PRIORITY = {l: p for (p, l) in
                   enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1)}
print(sum([LETTER_PRIORITY[l] for l in shared_letter]))

# Part 2
groups_of_three = [lines[i:i+3] for i in range(0, len(lines), 3)]
shared_letter = [[x for x in h[0] if x in h[1] and x in h[2]][0]
                 for h in groups_of_three]
print(sum([LETTER_PRIORITY[l] for l in shared_letter]))
