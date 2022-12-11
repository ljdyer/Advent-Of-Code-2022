with open('data.txt', 'r') as f:
    cmds = f.read().splitlines()[1:]

class Element:

    def __init__(self, name, type, size=None, parent=None):
        self.name = name
        self.type = type
        if type == 'dir':
            self.children = []
        else:
            self.size = size
        self.parent = parent
        self.level = parent.level + 1 if parent else 0

    def add_dir(self, name):
        self.children.append(Element(name, 'dir', parent=self))

    def add_file(self, name, size):
        self.children.append(Element(name, 'file', size, parent=self))
    
    def list_tree(self):
        if self.type == 'dir':
            print(f"{'  ' * self.level} - {self.name} (dir)")
            for child in self.children:
                child.list_tree()
        else:
            print(f"{'  ' * self.level} - {self.name} (file, size={self.size})")

    def calculate_dir_sizes(self):
        if self.type == 'file':
            return self.size
        else:
            self.size = sum([c.calculate_dir_sizes() for c in self.children])
            return self.size

    def get_dir_sizes(self):
        if self.type == 'dir':
            yield self.size
            for c in self.children:
                yield from c.get_dir_sizes()


root = Element('/', 'dir')
current_location = root

# Populate file system
while len(cmds) > 0:
    cmd = cmds.pop(0)
    if cmd == '$ ls':
        while cmds and not cmds[0].startswith('$'):
            pt1, pt2 = cmds.pop(0).split()
            if pt1.isnumeric():
                current_location.add_file(pt2, int(pt1))
            elif pt1 == 'dir':
                current_location.add_dir(pt2)
            else:
                raise ValueError()
    elif cmd == '$ cd ..':
        try:
            current_location = current_location.parent
        except:
            print(current_location)
    elif cmd.startswith('$ cd'):
        change_to = cmd.split()[2]
        current_location = [c for c in current_location.children if c.name == change_to][0]
    else:
        raise RuntimeError(f'Cmd not covered: {cmd}')
root.calculate_dir_sizes()

sizes = list(root.get_dir_sizes())

# Part One
print(f"Part One answer: {sum(s for s in sizes if s <= 100_000)}")

# Part Two
space_needed = root.size - 40_000_000
big_enough = [s for s in sizes if s >= space_needed]
print(f"Part Two answer: {min(big_enough)}")
