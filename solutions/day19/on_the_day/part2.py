from dataclasses import dataclass
from typing import Union, Tuple

# with open('../test_data.txt', 'r') as f:
with open('../data.txt', 'r') as f:
    data = f.read()


# ====================
def lt(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            return a<b
        elif isinstance(b, tuple):
            return a<b[0]
    elif isinstance(a, tuple):
        if isinstance(b, int):
            return a[0]<b
        elif isinstance(b, tuple):
            return a[0]<b[0]


# ====================
def join_if_adjacent_(z1, z2):
    if isinstance(z1, int):
        if isinstance(z2, int):
            if abs(z1 - z2) == 1:
                return tuple(sorted([z1, z2]))
        elif isinstance(z2, tuple):
            if abs(z1 - z2[0]) == 1:
                return (z1, z2[1])
            elif abs(z1 - z2[1]) == 1:
                return (z2[0], z1)
    if isinstance(z1, tuple):
        if isinstance(z2, int):
            if abs(z2 - z1[0]) == 1:
                return (z2, z1[1])
            elif abs(z1[1] - z2) == 1:
                return (z1[0], z2)
        elif isinstance(z2, tuple):
            if abs(z1[0] - z2[1]) == 1:
                return (z2[0], z1[1])
            elif abs(z2[0] - z1[1]) == 1:
                return (z1[0], z2[1])
    return None
        

# ====================
@dataclass
class Cube:
    x: Union[int, Tuple]
    y: Union[int, Tuple]
    z: Union[int, Tuple]
    def __lt__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return lt(self.z, other.z)
            else:
                return lt(self.y, other.y)
        else:
            return lt(self.x, other.x)
    def __repr__(self):
        return(f"({self.x}, {self.y}, {self.z})")
    def as_tuple(self):
        return (self.x, self.y, self.z)
    def join_if_adjacent(self, other):
        sx, sy, sz = self.as_tuple()
        ox, oy, oz = other.as_tuple()
        if sx == ox:
            if sy == oy:
                z = join_if_adjacent_(sz, oz)
                if z:
                    return Cube(sx, sy, z)
        return None
    def shift(self, n):
        if n == 1:
            return Cube(self.z, self.x, self.y)
        elif n == 2:
            return Cube(self.y, self.z, self.x)
        raise ValueError
    def __hash__(self):
        return hash(repr(self))


# ====================
def could_be_covered_(included):

    could_be_covered = []
    for i in range(len(included)-1):
        this, nxt = (included[i], included[i+1])
        if isinstance(this, int):
            if isinstance(nxt, int):
                could_be_covered.extend(list(range(this+1, nxt)))
            elif isinstance(nxt, tuple):
                could_be_covered.extend(list(range(this+1, nxt[0])))
        if isinstance(this, tuple):
            if isinstance(nxt, int):
                could_be_covered.extend(list(range(this[1]+1, nxt)))
            elif isinstance(nxt, tuple):
                could_be_covered.extend(list(range(this[1]+1, nxt[0])))
    return could_be_covered


# ====================
def included_by_point(joined):
    included_by_point = {}
    for c in joined:
        x,y,z = c.as_tuple()
        if (x,y) in included_by_point:
            included_by_point[(x,y)].append(z)
        else:
            included_by_point[(x,y)] = [z]
    return included_by_point


# ====================
def join_cubes(cubes_):
    cubes = cubes_.copy()
    joined = True
    while joined:
        for i in range(len(cubes)-1):
            joined_ = cubes[i].join_if_adjacent(cubes[i+1])
            if joined_:
                del cubes[i]
                del cubes[i]
                cubes.insert(i, joined_)
                break
        else:
            joined = False
    return cubes


# ====================
def get_points(xy, z):
    x, y = xy
    return [Cube(x, y, z_) for z_ in z]

cubes = sorted([Cube(*tuple(map(int, l.split(',')))) for l in data.splitlines()])

def surface_area(cubes):

    joined_s0 = join_cubes(cubes)
    shifted1 = sorted([c.shift(1) for c in cubes])
    joined_s1 = sorted(join_cubes(shifted1))
    shifted2 = sorted([c.shift(2) for c in cubes])
    joined_s2 = sorted(join_cubes(shifted2))
    surface_area = len(joined_s0)*2 + len(joined_s1)*2 + len(joined_s2)*2
    return(surface_area, joined_s0, joined_s1, joined_s2)

surface, joined_s0, joined_s1, joined_s2 = surface_area(cubes)
print(surface)

inc_s0 = included_by_point(joined_s0)
could_s0 = {k: could_be_covered_(v) for k, v in inc_s0.items()}
points_s0 = [p for xy, z in could_s0.items() for p in get_points(xy, z)]
could__s0 = sorted(points_s0)

inc_s1 = included_by_point(joined_s1)
could_s1 = {k: could_be_covered_(v) for k, v in inc_s1.items()}
points_s1 = [p for xy, z in could_s1.items() for p in get_points(xy, z)]
could__s1 = sorted([p.shift(2) for p in points_s1])

inc_s2 = included_by_point(joined_s2)
could_s2 = {k: could_be_covered_(v) for k, v in inc_s2.items()}
points_s2 = [p for xy, z in could_s2.items() for p in get_points(xy, z)]
could__s2 = sorted([p.shift(1) for p in points_s2])

covered = [c for c in could__s0 if (c in could__s1 and c in could__s2)]
print(len(covered))

covered = sorted(covered)
cubes.extend(covered)
cubes = sorted(list(set(cubes)))

surface, joined_s0, joined_s1, joined_s2 = surface_area(cubes)
print(joined_s0)
print(surface)