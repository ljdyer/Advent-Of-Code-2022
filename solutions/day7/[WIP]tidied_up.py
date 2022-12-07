from typing import Callable

# with open('test_data.txt', 'r') as f:
with open('data.txt', 'r') as f:
    cmds = f.read().splitlines()[1:]

class FileSystem:

    def __init__(self):
        self.system = {}
        self.current_dir_list = []

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
            print(' - /')
            dir_list = []
        current_dir = self.get_current_dir(dir_list)
        for k, v in current_dir.items():
            print('  ' * (len(dir_list)+1) + '- ' + k)
            if isinstance(v, dict):
                self.print_file_system(dir_list + [k])
    
    def get_size(self, update: Callable, dir_list: list = None):
        if dir_list is None:
            dir_list = []
        current_dir = self.get_current_dir(dir_list)
        if isinstance(current_dir, int):
            return current_dir
        else:
            
            return sum([self.get_size(dir_list + [k]) for k in current_dir.keys()])

    def get_smallest()
    
    
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
        raise RuntimeError(f'Cmd not covered: {cmd}')
# file_system.print_file_system()
# print(file_system.get_dirs_under_100_000())
MAX_SIZE = 70000000 - 30000000
required = file_system.get_size([]) - MAX_SIZE
file_system.print_file_system()
print(file_system.get_size([]))
# print(file_system.get_smallest(required))