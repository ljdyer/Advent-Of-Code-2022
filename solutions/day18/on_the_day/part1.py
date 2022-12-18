with open('../test_data.txt', 'r') as f:
# with open('../data.txt', 'r') as f:
    data = f.read()

cubes = [tuple(map(int, l.split(','))) for l in data.splitlines()]


# ====================
def join(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            return [a] + [b]
        elif isinstance(b, list):
            return [a] + b
    elif isinstance(a, list):
        if isinstance(b, int):
            return a + [b]
        if isinstance(b, list):
            return a + b
    raise ValueError(f"{type(a)} {type(b)}")



# ====================
def join_if_adjacent(z1, z2):
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

# =====
def join_cubes(cubes_):
    cubes = cubes_.copy()
    joined = True
    while joined:
        for i in range(len(cubes)-1):
            x1, y1, z1 = cubes[i]
            x2, y2, z2 = cubes[i+1]
            z = join_if_adjacent(z1, z2)
            if x1 == x2 and y1 == y2 and z:
                del cubes[i]
                del cubes[i]
                cubes.insert(i, (x1, y1, z))
                break
        else:
            joined = False
    print(cubes[:10])
    return cubes

# x,y,z
cubes = sorted(cubes)
o1 = join_cubes(cubes)
# y,z,x
cubes_ = sorted([(y,z,x) for x,y,z in cubes])
o2 = join_cubes(cubes_)
# z,x,y
cubes_ = sorted([(z,x,y) for x,y,z in cubes])
o3 = join_cubes(cubes_)

print(len(cubes) * 6)
print()
print(o1, o2, o3)
print(o1*2 + o2*2 + o3*2)