# with open('test_data.txt', 'r') as f:
with open('data.txt', 'r') as f:
    cmds = f.read().splitlines()[1:]

class FileSystem:

    def __init__(self):
        self.system = {}
        self.current_dir_list = []

    def __repr__(self):
        return str(self.system)

    def __str__(self):
        return str(self.system)

    def get_current_dir(self, dir_list):
        current_dir = self.system
        for dir in dir_list:
            current_dir = current_dir[dir]
        return current_dir
    
    def add_to_current_dir(self, k, v):
        current_dir = self.get_current_dir(self.current_dir_list)
        current_dir[k] = v

    def print_file_system(self, dir_list: list = None):
        if dir_list is None:
            dir_list = []
        current_dir = self.get_current_dir(dir_list)
        for k, v in current_dir.items():
            print('  - ' * (len(dir_list)+1) + k)
            if isinstance(v, dict):
                self.print_file_system(dir_list + [k])

    def get_dirs_under_100_000(self):
        self.total = 0
        self.add_to_total_if_under_100_000([])
        return self.total

    def add_to_total_if_under_100_000(self, dir_list: list = None):
        current_dir = self.get_current_dir(dir_list)
        for k, v in current_dir.items():
            if isinstance(v, dict):
                this_dir_size = self.dir_size(dir_list + [k])
                if this_dir_size < 100_000:
                    self.total += this_dir_size
                self.add_to_total_if_under_100_000(dir_list + [k])

    def get_smallest(self, required: int):
        self.required = required
        self.smallest = ([], self.dir_size([]))
        self.update_smallest()
        return self.smallest

    def update_smallest(self, dir_list: list = None):
        if dir_list is None:
            dir_list = []
        current_dir = self.get_current_dir(dir_list)
        for k, v in current_dir.items():
            if isinstance(v, dict):
                this_dir_size = self.dir_size(dir_list + [k])
                print(this_dir_size)
                if this_dir_size > self.required and this_dir_size < self.smallest[1]:
                    self.smallest = (dir_list + [k], this_dir_size)
                self.update_smallest(dir_list + [k])

    def dir_size(self, dir_list: list = None):
        if dir_list is None:
            dir_list = []
        current_dir = self.get_current_dir(dir_list)
        file_sizes = [v for v in current_dir.values() if isinstance(v, int)]
        dirs = [k for k, v in current_dir.items() if isinstance(v, dict)]
        return sum(file_sizes) + \
                sum([self.dir_size(dir_list + [d]) for d in dirs])



    
    
file_system = FileSystem()

while len(cmds) > 0:
    cmd = cmds.pop(0)
    if cmd == '$ ls':
        while cmds and not cmds[0].startswith('$'):
            file_or_dir = cmds.pop(0)
            if file_or_dir[0].isnumeric():
                size, fn = file_or_dir.split()
                file_system.add_to_current_dir(fn, int(size))
            else:
                _, dn = file_or_dir.split()
                file_system.add_to_current_dir(dn, {})
    elif cmd == '$ cd ..':
        file_system.current_dir_list = file_system.current_dir_list[:-1]
    elif cmd.startswith('$ cd'):
        change_to = cmd.split()[2]
        file_system.current_dir_list = file_system.current_dir_list + [change_to]
    else:
        print(cmd)
# file_system.print_file_system()
# print(file_system.get_dirs_under_100_000())
MAX_SIZE = 70000000 - 30000000
required = file_system.dir_size([]) - MAX_SIZE
print(required)
print(file_system.get_smallest(required))