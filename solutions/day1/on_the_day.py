with open('data.txt', 'r') as f:
    data = f.read().splitlines()

x = [[]]
while data:
    next_ = data.pop(0)
    if next_ == '':
        x.append([])
    else:
        x[-1].append(int(next_))

print(x)

sums = [sum(x_) for x_ in x]
print(sums)
xx = (sorted(sums))[-3:]
print(xx)
print(sum(xx))