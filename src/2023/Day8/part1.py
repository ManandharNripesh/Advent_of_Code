from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day8/test.txt")

directions = ""
nodes_left = {}
nodes_right = {}

for i, input_line in enumerate(input_lines):
    match i:
        case 0:
            directions = input_line.strip()
        case 1:
            continue
        case _:
            start_node, left_right = input_line.strip().split(" = ")
            left_right = left_right[1:-1]
            left, right = left_right.split(", ")
            nodes_left[start_node] = left
            nodes_right[start_node] = right

node = "AAA"
step = 0

while(node != "ZZZ"):
    dir = directions[step % len(directions)]
    if dir == "L":
        node = nodes_left[node]
    else:
        node = nodes_right[node]
    step += 1

print(step)