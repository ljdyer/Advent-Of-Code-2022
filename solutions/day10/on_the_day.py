# with open('test_data_2.txt', 'r') as f:
with open('data.txt', 'r') as f:
    instructions = f.read().splitlines()

X = 1
key_points = {k: None for k in [20, 60, 100, 140, 180, 220]}

queue = []
screen = []
for i in range(240):
    # Complete previous instructions
    if queue:
        do = queue.pop(0)
        if isinstance(do, int):
            X += do
    # Add next instruction
    if not queue:
        instruction = instructions.pop(0)
        print(instruction)
        if instruction == 'noop':
            queue = [None]
        if instruction.startswith('addx'):
            num = int(instruction.split()[1])
            queue = [None, num]
    if i % 40 in [X-1, X, X+1]:
        screen.append('#')
    else:
        screen.append('.')
    # if i+1 in key_points.keys():
    #     key_points[i+1] = X
    

# print(key_points)
# print(sum(
#     map(
#         lambda x: x[0]*x[1],
#         list(key_points.items())
#     )
# ))

screen_ = [screen[x:x+40] for x in range(0, 240, 40)]

for s in screen_:
    print(''.join(s))

