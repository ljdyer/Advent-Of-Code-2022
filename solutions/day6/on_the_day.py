with open('data.txt', 'r') as f:
    lines = f.read()

# ====================
def find_marker(buffer, x=14):

    buffer = list(buffer)
    last_four = buffer[:x]
    buffer = buffer[x:]
    last_char = x
    while True:
        if len(set(last_four)) == x:
            return last_char
        else:
            last_four = last_four[1:]
            last_four.append(buffer.pop(0))
            last_char += 1
        if not buffer:
            return None

print(find_marker(lines))
# for t in tests:
#     print(find_marker(t))