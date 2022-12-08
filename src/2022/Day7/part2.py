from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day7/test.txt")

root_dir = dict()
curr_dir = root_dir

for input_line in input_lines:
    words = input_line.strip().split(" ")

    if words[0] == "$":
        # process command
        if words[1] == "cd":
            if words[2] == "/":
                curr_dir = root_dir
            else:
                curr_dir = curr_dir[words[2]]
        else: # if words[1] == "ls":
            continue
    else:
        # process ls output
        if words[0] == "dir":
            curr_dir[words[1]] = dict()
            curr_dir[words[1]][".."] = curr_dir
        else:
            curr_dir[words[1]] = words[0]
            curr_dir.keys()

def sum_dir_sizes(dir):
    global total_size

    if type(dir) is not dict:
        return int(dir)

    size = 0
    for file in dir.keys():
        if file != "..":
            size += sum_dir_sizes(dir[file])

    return size

root_dir_size = sum_dir_sizes(root_dir)

free_space = 70000000 - root_dir_size
target_space = 30000000
minimum_size = target_space - free_space

target_size = 70000000

def find_smallest_dir(dir):
    global target_size

    if type(dir) is not dict:
        return int(dir)

    size = 0
    for file in dir.keys():
        if file != "..":
            size += find_smallest_dir(dir[file])

    if size >= minimum_size and size < target_size:
        target_size = size

    return size

find_smallest_dir(root_dir)

print(target_size)