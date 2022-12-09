with open('test_data_2.txt', 'r') as f:
# with open('data.txt', 'r') as f:
    movements = f.read().splitlines()    


movements = [x.split() for x in movements]
movements = [(x[0], int(x[1])) for x in movements]
print(movements)

T_positions = []

def plot_pos(H_pos, T_pos):

    x_max = 5
    y_max = 5
    matrix = [['.' for x in range(x_max)] for y in range(y_max)]
    matrix[T_pos[0]][T_pos[1]] = 'T'
    matrix[H_pos[0]][H_pos[1]] = 'H'
    for row in matrix:
        print(row)

def move(pos, dir):

    if dir == 'R':
        return(pos[0] + 1, pos[1])
    elif dir == 'L':
        return(pos[0] - 1, pos[1])
    elif dir == 'U':
        return(pos[0], pos[1] - 1)
    elif dir == 'D':
        return(pos[0], pos[1] + 1)
    else:
        raise ValueError('Bad direction')

from numpy import sign

def move_tail(H_pos, T_pos):

    x_dis = H_pos[0] - T_pos[0]
    y_dis = H_pos[1] - T_pos[1]
    if x_dis == 0:
        if abs(y_dis) <= 1:
            return T_pos
        elif y_dis == 2:
            return (T_pos[0], T_pos[1] + 1)
        elif y_dis == -2:
            return (T_pos[0], T_pos[1] - 1)
        else:
            raise ValueError('T more than 2 positions away!')
    elif y_dis == 0:
        if abs(x_dis) <= 1:
            return T_pos
        elif x_dis == 2:
            return (T_pos[0] + 1, T_pos[1])
        elif x_dis == -2:
            return (T_pos[0] - 1, T_pos[1])
        else:
            raise ValueError('T more than 2 positions away!')
    elif abs(x_dis) == 1 and abs(y_dis) == 1:
        return T_pos
    else:
        sign_x = sign(x_dis)
        sign_y = sign(y_dis)
        return (T_pos[0] + sign_x, T_pos[1] + sign_y)



H_pos = (0,0)
T_pos = (0,0)
T_positions.append(T_pos)
plot_pos(H_pos, T_pos)

# for m in movements:
#     dir, num = m
#     print(f'== {dir} {num} ==')
#     for _ in range(num):
#         H_pos = move(H_pos, dir)
#         T_pos = move_tail(H_pos, T_pos)
#         T_positions.append(T_pos)
#         # print(H_pos, T_pos)

# print(len(set(T_positions)))

knots = [(0,0) for _ in range(10)]
T_positions.append(knots[-1])
# plot_pos(H_pos, T_pos)

for m in movements:
    dir, num = m
    # print(f'== {dir} {num} ==')
    for _ in range(num):
        knots[0] = move(knots[0], dir)
        for i in range(1, len(knots)):
            knots[i] = move_tail(knots[i-1], knots[i])
        T_positions.append(knots[-1])
        
        # T_pos = move_tail(H_pos, T_pos)
        # print(H_pos, T_pos)

print(len(set(T_positions)))