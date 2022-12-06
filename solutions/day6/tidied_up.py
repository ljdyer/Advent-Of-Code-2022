with open('data.txt', 'r') as f:
    buffer = f.read()

# ====================
def find_marker(buffer, x):

    blocks = enumerate(
        [buffer[i:i+x] for i in range(len(buffer)-x+1)], 
        start=x
    )
    marker = next(block for block in blocks if len(set(block[1])) == x)[0]
    return marker


# Part 1
print(find_marker(buffer, 4))
# Part 2
print(find_marker(buffer, 14))
