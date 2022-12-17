from dataclasses import dataclass
import re

# with open('../test_data.txt', 'r') as f:
with open('../data.txt', 'r') as f:
    lines = f.read().splitlines()


"""The tall, vertical chamber is exactly seven units wide.
Each rock appears so that its left edge is two units away
from the left wall and its bottom edge is three units above
the highest rock in the room (or the floor, if there isn't one)."""

@dataclass 
class Shape:
    type: 1
    top: int
    left: int

grid_width = 7
grid_height = 0



def shape_points(shape):

    type = shape.type
    top = shape.top
    left = shape.left
    if type == 1:
        return [(top, left), (top, left+1), (top, left+2), (top, left+3)]
    elif type == 2:
        return [(top, left+1), (top+1, left), (top+1, left+1), (top+1, left+2), (top+2, left+1)]
    elif type == 3:
        return [(top, left+2), (top+1, left+2), (top+2, left), (top+2, left+1), (top+2, left+2)]
    elif type == 4:
        return [(top, left), (top+1, left), (top+2, left), (top+3, left)]
    elif type == 5:
        return [(top, left), (top, left+1), (top+1, left), (top+1, left+1)]

def touching(shape1, shape2):
    pass

def touching_floor(shape):

    shape_points_ = shape_points(shape)
    if any(r == 0 for r, c in shape_points_):
        return True
    return False







def draw_grid(shapes):

    floor = '+' + '-'*grid_width + '+'
    tops = [s.top for s in shapes]
    max_top = min(tops) - 1
    global grid_height
    grid_height = min(max_top, grid_height)
    print(grid_height)
    chamber = {n: ['.']*grid_width for n in range(grid_height, 1)}
    for s in shapes:
        shape_points_ = shape_points(s)
        print(shape_points_)
        for r, c in shape_points_:
            chamber[r][c] = '#'
    for r in range(grid_height, 1):
        print('|' + ''.join(chamber[r]) + '|')

    print(floor)
    

shapes = [Shape(type=1, top=-3, left=2)]
draw_grid(shapes)
while not touching_floor(shapes[-1]):
    shapes[-1].top += 1
    draw_grid(shapes)
shapes.append(Shape(type=2, top=-3, left=2))
while not touching_floor(shapes[-1]):
    shapes[-1].top += 1
    draw_grid(shapes)