with open('data.txt', 'r') as f:
    data = f.read().splitlines()

data = '|'.join(data).split('||')
data = [map(int, x.split('|')) for x in data]
sums = [sum(x) for x in data]

# Part 1
print(max(sums))

# Part 2
print(sum(sorted(sums)[-3:]))