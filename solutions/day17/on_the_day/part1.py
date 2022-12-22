from dataclasses import dataclass
import itertools
from copy import deepcopy

# with open('../test_data.txt', 'r') as f:
with open('../data.txt', 'r') as f:
    data = f.read()

jet_pattern = itertools.cycle(list(data))

"""The tall, vertical chamber is exactly seven units wide.
Each rock appears so that its left edge is two units away
from the left wall and its bottom edge is three units above
the highest rock in the room (or the floor, if there isn't one)."""

@dataclass 
class Shape:
    def __init__(self, type, top, left):

        self.type = type
        self.top = top
        self.left = left
        if type == 1:
            self.points = [(top, left), (top, left+1), (top, left+2), (top, left+3)]
        elif type == 2:
            self.points = [(top, left+1), (top+1, left), (top+1, left+1), (top+1, left+2), (top+2, left+1)]
        elif type == 3:
            self.points = [(top, left+2), (top+1, left+2), (top+2, left), (top+2, left+1), (top+2, left+2)]
        elif type == 4:
            self.points = [(top, left), (top+1, left), (top+2, left), (top+3, left)]
        elif type == 5:
            self.points = [(top, left), (top, left+1), (top+1, left), (top+1, left+1)]

    def __repr__(self):

        return str(self.points)

    def move_down(self):

        self.top += 1
        self.points = [(x+1, y) for x, y in self.points]

    def move_left(self):

        self.left -= 1
        self.points = [(x, y-1) for x, y in self.points]

    def move_right(self):

        self.left += 1
        self.points = [(x, y+1) for x, y in self.points]

    def bottom(self):

        return max(x[0] for x in self.points)
        
    def right(self):

        return max(x[1] for x in self.points)

    def move_left_or_right(self, dir):

        if dir == '>':
            if self.right() < grid_width-1:
                # print('Pushed right.')
                self.move_right()
            else:
                pass
                # print('Pushed right, but nothing happens')
        if dir == '<':
            if self.left > 0:
                # print('Pushed left.')
                self.move_left()
            else:
                pass
                # print('Pushed left, but nothing happens')
        return self

    def would_touch(self, points_covered):

        # Would touch floor
        if self.bottom() > 0:
            return True
        else:
            if any([p in points_covered for p in self.points]):
                    return True
        return False

def remove_irrelevant_points(points):

    top_row = max_top(points)
    
    return [p for p in points if p[0] < top_row + 100]

def new_top(shape_type, current_top):
    if shape_type == 1:
        return current_top - 1
    if shape_type in [2, 3]:
        return current_top - 3
    if shape_type == 4:
        return current_top - 4
    if shape_type == 5:
        return current_top - 2

grid_width = 7

def max_top(points_covered, new_shape=None):

    top = min([p[0] for p in points_covered], default=1)
    if new_shape:
        top = min([new_shape.top, top])
    return top


def draw_grid(points_covered, new_shape):

    floor = '+' + '-'*grid_width + '+'
    max_top_ = max_top(points_covered, new_shape)
    chamber = {n: ['.']*grid_width for n in range(max_top_, 1)}
    print(chamber)
    for r, c in points_covered:
        chamber[r][c] = '#'
    shape_points_ = new_shape.points
    for r, c in shape_points_:
        chamber[r][c] = '@'
    for r in range(max_top_, 1):
        print('|' + ''.join(chamber[r]) + '|')
    print(floor)
    
points_covered = []
shape_types = itertools.cycle(range(1,6))

for n in range(2022):

    next_shape_type = next(shape_types)
    max_top_ = max_top(points_covered)
    new_shape = Shape(type=next_shape_type, top=new_top(next_shape_type, max_top_)-3, left=2)
    while True:
        # Jet
        new_new_shape = deepcopy(new_shape)
        new_new_shape.move_left_or_right(next(jet_pattern))
        if not new_new_shape.would_touch(points_covered):
            new_shape = new_new_shape
        # Fall
        new_new_shape = deepcopy(new_shape)
        new_new_shape.move_down()
        if not new_new_shape.would_touch(points_covered):
            new_shape = new_new_shape
        else:
            points_covered.extend(new_shape.points)
            points_covered = remove_irrelevant_points(points_covered)
            # draw_grid(points_covered, new_shape)
            break
    print(n)

height = -max_top(points_covered) + 1
print(height)