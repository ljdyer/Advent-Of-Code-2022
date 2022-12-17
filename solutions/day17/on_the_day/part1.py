from dataclasses import dataclass
import itertools
import re

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
    type: 1
    top: int
    left: int
    def points(self):
        type = self.type
        top = self.top
        left = self.left
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

    def touching(self, other):
        self_points = self.points()
        other_points = other.points()
        print(self_points)
        print(other_points)
        for r, c in self_points:
            if (r+1, c) in other_points:
                print('touching')
                return True
        return False

    def touching_floor(self):
        points = self.points()
        if any(r == 0 for r, c in points):
            return True
        return False

    def bottom(self):
        pass

    def right(self):




grid_width = 7


def max_top(shapes):

    tops = [s.top for s in shapes]
    max_top = min(tops, default=0)
    return max_top


def diff_top_bottom(shape_type):

    if shape_type == 1:
        return 0
    if shape_type in [2, 3]:
        return 2
    if shape_type == 5:
        return 1
    if shape_type == 4:
        return 3



def draw_grid(shapes):

    floor = '+' + '-'*grid_width + '+'
    max_top_ = max_top(shapes)
    chamber = {n: ['.']*grid_width for n in range(max_top_, 1)}
    for s in shapes[:-1]:
        shape_points_ = s.points()
        for r, c in shape_points_:
            chamber[r][c] = '#'
    shape_points_ = shapes[-1].points()
    for r, c in shape_points_:
        chamber[r][c] = '@'
    for r in range(max_top_, 1):
        print('|' + ''.join(chamber[r]) + '|')

    print(floor)
    
shapes = []
shape_types = itertools.cycle(range(1,6))

for _ in range(2):
    next_shape_type = next(shape_types)
    next_top = max_top(shapes)
    shapes.append(Shape(type=next_shape_type, top=next_top-4-diff_top_bottom(next_shape_type), left=2))
    draw_grid(shapes)
    while not shapes[-1].touching_floor() and not any(shapes[-1].touching(s) for s in shapes[:-1]):

        shapes[-1].top += 1
        draw_grid(shapes)