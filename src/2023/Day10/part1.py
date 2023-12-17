from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day10/test.txt")

pipe_map = []
start_pos = (-1,-1)


for i, input_line in enumerate(input_lines):
    pipe_map.append(input_line)

    if "S" in input_line:
        start_pos = (i, input_line.index("S"))

positions = []
dirs = []

for offset in range(-1, 2, 2):
    # check vertically
    i = start_pos[0] + offset
    j = start_pos[1]

    if i >= 0 and i < len(pipe_map):
        if offset < 0:
            if pipe_map[i][j] in "|7F":
                positions.append((i, j))
                dirs.append("N")
        else: #elif offset > 0:
            if pipe_map[i][j] in "|LJ":
                positions.append((i, j))
                dirs.append("S")
    
    # check horizontally
    i = start_pos[0]
    j = start_pos[1] + offset

    if j >= 0 and j < len(pipe_map):
        if offset < 0:
            if pipe_map[i][j] in "-LF":
                positions.append((i, j))
                dirs.append("W")
        else: #elif offset > 0:
            if pipe_map[i][j] in "-J7":
                positions.append((i, j))
                dirs.append("E")

dist = 1

while positions[0] != positions[1]:
    next_positions = positions.copy()
    next_dirs = dirs.copy()

    for pos_num in range(len(positions)):
        i, j = positions[pos_num]
        match pipe_map[i][j]:
            case "|":
                match dirs[pos_num]:
                    case "N":
                        next_positions[pos_num] = (i-1, j)
                    case "S":
                        next_positions[pos_num] = (i+1, j)
            case "-":
                match dirs[pos_num]:
                    case "W":
                        next_positions[pos_num] = (i, j-1)
                    case "E":
                        next_positions[pos_num] = (i, j+1)
            case "L":
                match dirs[pos_num]:
                    case "W":
                        next_positions[pos_num] = (i-1, j)
                        next_dirs[pos_num] = "N"
                    case "S":
                        next_positions[pos_num] = (i, j+1)
                        next_dirs[pos_num] = "E"
            case "J":
                match dirs[pos_num]:
                    case "E":
                        next_positions[pos_num] = (i-1, j)
                        next_dirs[pos_num] = "N"
                    case "S":
                        next_positions[pos_num] = (i, j-1)
                        next_dirs[pos_num] = "W"
            case "7":
                match dirs[pos_num]:
                    case "E":
                        next_positions[pos_num] = (i+1, j)
                        next_dirs[pos_num] = "S"
                    case "N":
                        next_positions[pos_num] = (i, j-1)
                        next_dirs[pos_num] = "W"
            case "F":
                match dirs[pos_num]:
                    case "W":
                        next_positions[pos_num] = (i+1, j)
                        next_dirs[pos_num] = "S"
                    case "N":
                        next_positions[pos_num] = (i, j+1)
                        next_dirs[pos_num] = "E"
    
    if positions[0] == next_positions[1]:
        break
    positions = next_positions.copy()
    dirs = next_dirs.copy()
    dist += 1

print(dist)